from hashlib import sha1
import pandas as pd
import pytest
import altair
import sys
import numpy as np

def test_0_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (38982, 14), "Your dataframe dimensions are incorrect. Are you reading in the 'world-data-gapminder' data?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns))[0:4] == ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], msg
    assert "Africa" in list(
        answer.region
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.income)
    ) == 176476505, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return("Success")

def test_0_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert str(answer['year'].dtype) == 'datetime64[ns]', "Make sure you are parsing the year column as a 'datetime' object."
    return("Success")


def test_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(len(answer)).encode('utf8')).hexdigest() == "da4b9237bacccdf19c0760cab7aec4a8359010b0", "The number of correct solutions is incorrect. Please try again"
    assert sha1(str(sorted([x.lower() for x in answer])).encode('utf8')).hexdigest() == "d24a1f998b412db6fb30918e1382f00ffa79bb8e", "Your answer is incorrect. Please try again."
    return("Success")

def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "w").encode('utf8')).hexdigest() == "8e425ff79c7c294266f1a4093c553d06af472609", "Your answer is incorrect. Please try again."
    return("Success")

def test_1_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "k").encode('utf8')).hexdigest() == "b86f6db284d374188d561d46b45b188d5631609a", "Your answer is incorrect. Please try again. Are you examining the plots correctly?"
    return("Success")

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "x").encode('utf8')).hexdigest() == "6eeb3fecf98e6cb569171a38808fac301b190eab", "Your answer is incorrect. Please try again."
    return("Success")

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "z").encode('utf8')).hexdigest() == "90283840d90de49b8e7984bd99b47fee0d4bd50d", "Your answer is incorrect. Please try again."
    return("Success")

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "a").encode('utf8')).hexdigest() == "cdd4f874095045f4ae6670038cbbd05fac9d4802", "Your answer is incorrect. Please try again."
    return("Success")

def test_1_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(len(answer)).encode('utf8')).hexdigest() == "da4b9237bacccdf19c0760cab7aec4a8359010b0", "The number of correct solutions is incorrect. Please try again"
    assert sha1(str(sorted([x.lower() for x in answer])).encode('utf8')).hexdigest() == "98f57b79cc1f11e85a800332d9bb015e2aaa8ef4", "Your answer is incorrect. Please try again."
    return("Success")

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (1068, 14), "Your dataframe dimensions are incorrect. Are you subsetting the data correctly?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns))[0:4] == ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], msg
    assert "Africa" in list(
        answer.region
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.income)
    ) == 9195497, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return("Success")

def test_2_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.data.groupby('country').count().loc['Afghanistan','year'] == 6, "Are you using the 'gapminder_every20' dataset?"
    assert answer.mark == 'circle', "Make sure you are creating a scatter plot using the 'mark.circle()' function."
    assert answer.encoding.x.shorthand == 'children_per_woman' or answer.encoding.x.field == 'children_per_woman', "Make sure you are plotting 'children_per_woman' on the x-axis."
    assert answer.encoding.y.shorthand == 'child_mortality' or answer.encoding.y.field == 'child_mortality', "Make sure you are plotting 'child_mortality' on the y-axis."
    assert answer.encoding.color.shorthand == 'income_group' or answer.encoding.color.field == 'income_group', "Make sure you are coloring by 'income_group'."
    return ("Success")

def test_2_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return("Success")

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.facet.shorthand == 'year' or answer.facet.field == 'year', "Make sure the plot is faceted based on 'year'."
    return ("Success")

def test_2_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(len(answer)).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "The number of correct solutions is incorrect. Please try again"
    assert sha1(str(sorted([x.lower() for x in answer])).encode('utf8')).hexdigest() == "00dd0637ea7a465c83c8998839813d71f0f956a3", "Your answer is incorrect. Please try again. Are you examining the plots correctly?"
    return("Success")

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "39e21432a7dcba489697b4ef779f4b0c6f08b89f", "Your answer is incorrect. The 'max' and 'isna()' functions might be useful here."
    return("Success")

def test_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (178, 14), "Your dataframe dimensions are incorrect. Are you subsetting the data correctly?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns))[0:4] == ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], msg
    assert "Africa" in list(
        answer.region
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.income)
    ) == 3003677, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert str(set(list(answer.year))) == "{Timestamp('2014-01-01 00:00:00')}", "Make sure you are keeping only the desired years."
    return("Success")

def test_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (40, 14), "Your dataframe dimensions are incorrect. Are you subsetting the data correctly?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns))[0:4] == ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], msg
    assert "Africa" in list(
        answer.region
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.income)
    ) == 1550000, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert max(list(answer.co2_per_capita)) == 45.4, "The maximum value for 'co2_per_capita' is incorrect. Are you selecting the top 40?"
    assert min(list(answer.co2_per_capita)) == 6.19, "The minimum value for 'co2_per_capita' is incorrect. Are you selecting the top 40?"
    return("Success")

def test_3_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar', "Make sure you are creating a bar plot using the 'mark.bar()' function."
    assert answer.encoding.x.shorthand == 'co2_per_capita' or answer.encoding.x.field == 'co2_per_capita', "Make sure you are plotting 'co2_per_capita' on the x-axis."
    assert answer.encoding.y.shorthand == 'country' or answer.encoding.y.field == 'country', "Make sure you are plotting 'country' on the y-axis."
    assert answer.encoding.color.shorthand == 'region' or answer.encoding.color.field == 'region', "Make sure you are coloring by 'region'."
    return ("Success")

def test_3_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    assert answer.encoding.y.sort == 'x' or answer.encoding.y.sort == 'x', "Make sure you are sorting the y-axis based on x-axis values."
    return("success")

def test_3_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == "133f5f567509940df6c46c9597e28f976a75fa71", "Your answer is incorrect. Please try again. Are you examining the plots correctly?"
    return("Success")

def test_3_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "da4b9237bacccdf19c0760cab7aec4a8359010b0", "Your answer is incorrect. Please try again. Are you examining the plots correctly?"
    return("Success")


def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (38982, 15), "Your dataframe dimensions are incorrect. Are you adding the new column?"
    assert "co2_total" in list(answer.columns), "Make sure you are adding 'co2_total' as a new column"
    assert np.nanmax(list(answer.co2_total)) == 10286000000.0, "The maximum value for 'co2_total' is incorrect. Are you computing this value correctly?"
    assert np.nanmin(list(answer.co2_total))  == 0.0, "The maximum value for 'co2_total' is incorrect. Are you computing this value correctly?"
    return("Success")

def test_3_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (40, 15), "Your dataframe dimensions are incorrect. Are you subsetting the data correctly?"
    assert str(set(list(answer.year))) == "{Timestamp('2014-01-01 00:00:00')}", "Your date column contains the incorrect years. Are you filtering out the correct years?"
    return("Success")
    assert np.nanmax(list(answer.co2_total)) == 10286000000.0, "The maximum value for 'co2_total' is incorrect. Are you selecting the top 40?"
    assert np.nanmin(list(answer.co2_total)) == 95256000.0, "The minimum value for 'co2_total' is incorrect. Are you selecting the top 40?"
    return("Success")

def test_3_10_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar', "Make sure you are creating a bar plot using the 'mark.bar()' function."
    assert answer.encoding.x.shorthand == 'co2_total' or answer.encoding.x.field == 'co2_total', "Make sure you are plotting 'co2_total' on the x-axis."
    assert answer.encoding.y.shorthand == 'country' or answer.encoding.y.field == 'country', "Make sure you are plotting 'country' on the y-axis."
    assert answer.encoding.color.shorthand == 'region' or answer.encoding.color.field == 'region', "Make sure you are coloring by 'region'."
    assert answer.encoding.y.sort == 'x' or answer.encoding.y.sort == 'x', "Make sure you are sorting the y-axis based on x-axis values."
    return ("Success")


def test_3_10_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return("Success")

def test_3_11(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == "3ab9380fa2521f2d0d94fe931b79a1e1eaa91890", "Your answer is incorrect. Please try again. Are you examining the plot correctly?"
    return("Success")

def test_3_12(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(int(answer)).encode('utf8')).hexdigest() == "91032ad7bbcb6cf72875e8e8207dcfba80173f7c", "Your answer is incorrect. Please try again."
    return("Success")

def test_3_13_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'area', "Make sure you are creating an area plot using the 'mark.area()' function."
    assert answer.encoding.x.shorthand == 'year' or answer.encoding.x.field == 'year', "Make sure you are plotting 'year' on the x-axis."
    assert answer.encoding.y.field, "Make sure you are plotting 'sum(co2_total)' on the y-axis."
    assert answer.encoding.color.shorthand == 'region' or answer.encoding.color.field == 'region', "Make sure you are coloring by 'region'."
    return ("Success")


def test_3_13_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return("Success")

def test_3_14(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + 'p').encode('utf8')).hexdigest() == "3f81e91d69a8a61ffbf19297eb0791ad54ce5690", "Your answer is incorrect. Please try again. Are you examining the plot correctly?"
    return("Success")

def test_3_15(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == "79be276817ebcd106b9fc3d227e18059faf7790e", "Your answer is incorrect. Please try again. Are you examining the plot correctly?"
    return("Success")

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (356, 14), "Your dataframe dimensions are incorrect. Are you subsetting the data correctly?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns))[0:4] == ['child_mortality', 'children_per_woman', 'co2_per_capita', 'country'], msg
    assert "Africa" in list(
        answer.region
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.income)
    ) == 5085804, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert str(set(list(answer.year))) == "{Timestamp('2014-01-01 00:00:00'), Timestamp('1979-01-01 00:00:00')}" or str(set(list(answer.year))) == "{Timestamp('1979-01-01 00:00:00'), Timestamp('2014-01-01 00:00:00')}", "Make sure you are keeping only the desired years."
    return("Success")

def test_4_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'circle', "Make sure you are creating a scatter plot using the 'mark.circle()' function."
    assert answer.encoding.x.shorthand == 'income' or answer.encoding.x.field == 'income', "Make sure you are plotting 'income' on the x-axis."
    assert answer.encoding.y.shorthand == 'co2_per_capita' or answer.encoding.y.field == 'co2_per_capita', "Make sure you are plotting 'co2_per_capita' on the y-axis."
    assert answer.encoding.color.shorthand == 'region' or answer.encoding.color.field == 'region', "Make sure you are coloring by 'region'."
    return ("Success")

def test_4_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return("Success")

def test_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.facet.shorthand == 'year' or answer.facet.field == 'year' or answer.facet.column == 'year' or answer.facet.row == 'year', "Make sure the plot is faceted based on 'year'."
    return ("Success")

def test_4_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == "fb360f9c09ac8c5edb2f18be5de4e80ea4c430d0", "Your answer is incorrect. Please try again. Are you examining the plots correctly?"
    return("Success")
