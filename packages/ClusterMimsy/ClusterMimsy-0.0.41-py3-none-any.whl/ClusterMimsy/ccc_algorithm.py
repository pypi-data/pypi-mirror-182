import sys

import pandas as pd
import numpy as np

from itertools import combinations

from sklearn.metrics import mutual_info_score


# All functions

def get_partition_from_column_names(data, columns_in_partition):
    return data[columns_in_partition]


def combine_partition_columns(columns_in_partition1, columns_in_partition2):
    return columns_in_partition1.union(columns_in_partition2)


def _assertions_for_entropy(probabilities: pd.Series, cardinality):
    assert np.isclose(1.0, probabilities.sum()), 'Probabilities should sum to 1'
    assert probabilities.le(1.0).all(), 'Probabilities should all be less than or equal to 1'
    assert not (probabilities.le(0.0).any()), 'Probabilities should all be greater than 0'
    assert type(cardinality) == int
    assert cardinality >= 1


def entropy(probabilities: pd.Series, cardinality=2):
    _assertions_for_entropy(probabilities, cardinality)

    # Handling for the case that there is a cardinality that isn't
    logged_probabilities = np.log2(probabilities) / np.log2(cardinality)

    # Calculate shannon entropy
    _entropies = probabilities * logged_probabilities
    entropy = -_entropies.sum()
    return entropy


def get_mutual_information_data_frame_from_data_frame(dataframe):
    # Create the dataframe to be returned
    mutual_information_dataframe = pd.DataFrame(index=dataframe.columns,
                                                columns=dataframe.columns)

    # Fill diagonal (entropy of each column)
    for column in dataframe.columns:
        column_entropy = mutual_info_score(dataframe[column], dataframe[column])
        mutual_information_dataframe[column][column] = column_entropy

    # Fill off-diagonals (mutual information)
    all_column_combinations = list(combinations(dataframe.columns, 2))
    for column_combination in all_column_combinations:
        column_1, column_2 = column_combination
        _mi = mutual_info_score(dataframe[column_1], dataframe[column_2])
        mutual_information_dataframe[column_1][column_2] = _mi
        mutual_information_dataframe[column_2][column_1] = _mi

    return mutual_information_dataframe


def mutual_information_between_two_partitions(mutual_information_dataframe: pd.DataFrame, partition1: set,
                                              partition2: set):
    assert partition1.isdisjoint(partition2), 'Two partitions should not share a column name.'

    # Mutual information will be averaged over all combinations
    size_partition_1, size_partition_2 = len(partition1), len(partition2)
    divider = size_partition_1 * size_partition_2

    # sum mutual information over the cartesian product of the sets
    sum_of_mi = 0
    for column_i in partition1:
        for column_j in partition2:
            sum_of_mi += mutual_information_dataframe[column_i][column_j]

    return sum_of_mi / divider


def entropy_of_one_partition(dataframe, partition, cardinality=2):
    partitioned_df = dataframe[partition]

    count_of_unique_rows = (partitioned_df.groupby(list(partition)).size().reset_index(name='Count')['Count'])
    probabilities_for_unique_rows = (count_of_unique_rows
                                     / count_of_unique_rows.sum())

    return count_of_unique_rows.sum() * entropy(probabilities_for_unique_rows, cardinality)


def complexity_model(dataframe, partitions, cardinality=2):
    num_samples = dataframe.shape[0]
    scalar = np.log2(num_samples + 1) / np.log2(cardinality)

    model_complexity = 0
    for partition in partitions:
        partition_complexity = (cardinality ** len(partition)) - 1
        model_complexity += partition_complexity

    return scalar * model_complexity


def complexity_population(dataframe, partitions, cardinality=2):
    population_complexity = 0
    for partition in partitions:
        entropy_of_partition = entropy_of_one_partition(dataframe, partition, cardinality)
        population_complexity += entropy_of_partition
    return population_complexity


def obey_partitions_threshold(dataframe, partitions, cardinality=2):
    num_samples = dataframe.shape[0]
    for partition in partitions:
        if (cardinality ** len(partition)) > num_samples:
            return False
    return True


def combined_complexity(dataframe, partitions, cardinality=2):
    """
    https://courses.physics.illinois.edu/phys466/sp2013/projects/2000/team8/node5.html
    """
    all_partition_combinations = combinations(partitions, 2)
    for partition_combination in all_partition_combinations:
        partition1, partition2 = partition_combination
        assert partition1.isdisjoint(partition2), (
            f"""Two partitions should not share a column name. \n
             Shared column name(s) {partition1.intersection(partition2)} in partitions {partition1} and {partition2}""")

    cp = complexity_population(dataframe, partitions, cardinality)
    cm = complexity_model(dataframe, partitions, cardinality)
    ccc = cp + cm

    is_as_acceptable_solution = obey_partitions_threshold(dataframe, partitions, cardinality)

    return ccc, is_as_acceptable_solution


def get_partition_probabilities(dataframe, partition):
    partitioned_df = dataframe[partition]

    num_samples = dataframe.shape[0]

    unique_rows = (partitioned_df
                   .groupby(list(partition))
                   .size()
                   .reset_index(name='Probability'))

    unique_rows['Probability'] = unique_rows['Probability'] / num_samples

    return unique_rows.sort_values(['Probability'], ascending=False)


def get_all_partition_probabilities(dataframe, partitions, verbose=False):
    partition_probabilities = []
    for partition in partitions:
        _partition_probabilities = get_partition_probabilities(dataframe, partition)
        partition_probabilities.append(_partition_probabilities)
        if verbose:
            print(_partition_probabilities, '\n')
    return partition_probabilities


def get_cardinality(dataframe):
    possible_cardinalities = dataframe.nunique()
    # are they all equal
    if (possible_cardinalities == possible_cardinalities[0]).all():
        cardinality = possible_cardinalities[0]
        return min(cardinality, 2)
    elif (possible_cardinalities <= 2).all():
        return 2
    else:
        maximum_cardinality = possible_cardinalities.max()
        minimum_cardinality = possible_cardinalities.min()
        sys.exit(f"""
    Assertion Error: There was a mismatch of cardinalities, with
    If the columns do not have the same cardinalities (eg.all binary, all trinary etc), then the formulas used are not
    appropriate.
    You can still run the analysis by specifying a cardinality between
        maximum cardinality: {maximum_cardinality}
        minimum cardinality: {max(minimum_cardinality, 2)}
    Alternatively, limit the analysis to a dataframe with all the same cardinality. All column cardinalities are:
    {possible_cardinalities}
    """)


def initial_partitions(dataframe):
    partitions = []
    for column in dataframe.columns:
        partitions.append({column})
    return partitions


def _update_step_for_clustermimsy(dataframe, best_partitions, best_ccc, mi_df, cardinality):
    possible_improvement, best_combination = False, None
    best_mi = 0
    for combination in combinations(best_partitions, 2):
        partition1, partition2 = combination
        mi = mutual_information_between_two_partitions(mi_df,
                                                       partition1, partition2)
        if mi > best_mi:
            best_combination = combination
            best_mi = mi
            possible_improvement = True
    if possible_improvement:
        # Suggest a new model structure with the highest MI partitions combined
        partition1, partition2 = best_combination
        query_partitions = best_partitions.copy()
        query_partitions.remove(partition1)
        query_partitions.remove(partition2)
        query_partitions.append(combine_partition_columns(partition1, partition2))

        query_ccc, acceptance = combined_complexity(dataframe,
                                                    query_partitions,
                                                    cardinality)

        if (acceptance) and (query_ccc < best_ccc):
            return query_partitions, query_ccc, True
        else:
            return best_partitions, best_ccc, False
    else:
        return best_partitions, best_ccc, False


def _update_loop_for_clustermimsy(dataframe, best_partitions, best_ccc, mi_df, cardinality, verbose=False):
    to_continue = True
    while to_continue:
        if verbose:
            print(best_partitions, best_ccc, to_continue)
        best_partitions, best_ccc, to_continue = _update_step_for_clustermimsy(dataframe, best_partitions, best_ccc,
                                                                               mi_df, cardinality)
    if verbose:
        print(best_partitions, best_ccc, to_continue)
    return best_partitions, best_ccc


def clustermimsy(dataframe, cardinality=None, verbose=False):
    # sort out cardinality
    if cardinality is not None:
        assert type(cardinality) is int, 'cardinality must be of type int'
        assert cardinality >= 2, 'cardinality must be at least 2'
    else:
        cardinality = get_cardinality(dataframe)

    # set up mutual information dataframe
    mi_df = get_mutual_information_data_frame_from_data_frame(dataframe)

    # set up starting partitions
    best_partitions = initial_partitions(dataframe)

    # initial CCC
    best_ccc, initial_acceptance = combined_complexity(dataframe,
                                                       best_partitions,
                                                       cardinality)
    assert initial_acceptance, 'You must have at least a number of rows in your data frame greater than the cardinality used'

    # iteration loop
    best_partitions, best_ccc = _update_loop_for_clustermimsy(dataframe, best_partitions, best_ccc, mi_df, cardinality,
                                                              verbose)

    return best_partitions
