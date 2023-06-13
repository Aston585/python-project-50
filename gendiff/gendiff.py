from gendiff.loading import loading_data
from gendiff.comparer import get_comparison_results
from gendiff.formaters.stylish import stylish_view
from gendiff.formaters.plain import flatten
from gendiff.formaters.json_ import json_viev


def generate_diff(data1, data2, format='stylish'):
    source1 = loading_data(data1)
    source2 = loading_data(data2)
    diff = get_comparison_results(source1, source2)
    if format == 'plain':
        return flatten(diff)(diff)
    elif format == 'json':
        return json_viev(diff)
    return stylish_view(diff)
