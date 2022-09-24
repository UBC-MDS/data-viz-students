from hashlib import sha1
import pandas as pd
import pytest
import sys
import numpy as np
import re
import altair as alt

success = "Success"

def test_titles(answer):
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)


def test_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (4451, 2), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['dissatisfaction_last_year', 'dissatisfaction_this_year'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['dissatisfaction_last_year', 'dissatisfaction_this_year'], msg
    assert round(sum(
        list(answer.dissatisfaction_this_year)
    )) == 836, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert round(sum(
        list(answer.dissatisfaction_last_year)
    )) == 986, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "3c43d40a064773eacde7fb2b19673970d406d1f6", "Your answer is incorrect. Please try again."
    return(success)

def test_1_2_old(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 5, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "7a475469311b4cc276c05507d630bad34d28a13a", "Your answer is incorrect. Please try again."
    return(success)


def test_1_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.mark.color.encode('utf8')).hexdigest() == "bc74f4f071a5a33f00ab88a6d6385b5e6638b86c", "The color is incorrect. Are you examining the original plot correctly?"
    assert sha1(str(answer.mark.size).encode('utf8')).hexdigest() == "310b86e0b62b828562fc91c7be5380a992b2786a", "The points size is incorrect. Are you examining the original plot correctly?"
    assert sha1(answer.mark.type.encode('utf8')).hexdigest() == "00b7b8118efde44c546b69243ec15b21cd64c9d9", "The plot type is incorrect. Are you examining the plot original correctly?"
    return(success)


def test_1_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.encoding.x.field.encode('utf8')).hexdigest() == "09ade1377f03dadec1de00aaa6fd4ac215edac2c", "Your x-axis is incorrect. Are you examining the original plot correctly?"
    assert sha1(answer.encoding.y.field.encode('utf8')).hexdigest() == "02cd3b107a9c91476522398de1fd67d78fffb72d", "Your y-axis is incorrect. Are you examining the original plot correctly?"
    return(success)


def test_1_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.title.text.strip().encode('utf8')).hexdigest() == "a14a9d1b06af5f02ce76873ddb919e1d0ec5c62f", "Your plot title is incorrect. Are you examining the original plot correctly?"
    assert sha1(answer.title.subtitle.strip().encode('utf8')).hexdigest() == "8effba3e3a11d79e3352f8889e0f9069d4368702", "Your plot subtitle is incorrect. Are you examining the original plot correctly?"
    return(success)


def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'rect', "Make sure you are creating a 2D histogram plot using the 'mark_rect()' function."
    assert answer.encoding.x.bin.maxbins == 30, "Make sure you are setting the maxbins on the x-axis to 30."
    assert answer.encoding.y.bin.maxbins == 30, "Make sure you are setting the maxbins on the y-axis to 30."
    assert answer.encoding.y.bin.extent == (0, 1), "Make sure you are setting the bin extent between (0, 1)."
    assert answer.encoding.x.shorthand == 'dissatisfaction_last_year' or answer.encoding.x.field == 'dissatisfaction_last_year', "Make sure you are plotting 'dissatisfaction_last_year' on the x-axis."
    assert answer.encoding.x.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative."
    assert answer.encoding.y.shorthand == 'dissatisfaction_this_year' or answer.encoding.y.field == 'dissatisfaction_this_year', "Make sure you are plotting 'dissatisfaction_this_year' on the y-axis."
    assert answer.encoding.y.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    assert not str(type(answer.title.subtitle[0])) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a subtitle for your plot."
    assert not answer.title.subtitle[0].islower(), "Make sure the plot title is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot title does not contain underscores."
    assert answer.encoding.color.aggregate == 'count', "Make sure you are coloring by count."
    return(success)

def test_1_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'rect', "Make sure you are creating a 2D histogram plot using the 'mark_rect()' function."
    assert answer.encoding.x.shorthand == 'dissatisfaction_last_year' or answer.encoding.x.field == 'dissatisfaction_last_year', "Make sure you are plotting 'dissatisfaction_last_year' on the x-axis."
    assert answer.encoding.x.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative."
    assert answer.encoding.y.shorthand == 'dissatisfaction_this_year' or answer.encoding.y.field == 'dissatisfaction_this_year', "Make sure you are plotting 'dissatisfaction_this_year' on the y-axis."
    assert answer.encoding.y.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative."
    assert answer.encoding.color.aggregate == 'count', "Make sure you are coloring by count."
    return(success)

def test_1_5_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.x.bin.maxbins == 30, "Make sure you are setting the maxbins on the x-axis to 30."
    assert answer.encoding.y.bin.maxbins == 30, "Make sure you are setting the maxbins on the y-axis to 30."
    assert answer.encoding.y.bin.extent == (0, 1), "Make sure you are setting the bin extent between (0, 1)"
    return(success)

def test_1_5_3(answer):
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert not answer.encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>",  "Make sure you are providng a title for your plot."
    assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.to_dict()['subtitle'] == None, "Make sure you are providng a subtitle for your plot."
    assert not answer.title.subtitle[0].islower(), "Make sure the plot title is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot title does not contain underscores."
    return(success)

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 't').encode('utf8')).hexdigest() == '589e942e00a7dd64a273deb5041c7ce469f2bad7', "Your answer is incorrect. Please try again. Are you examining the plot?"
    return(success)

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'p').encode('utf8')).hexdigest() == '881baaede9ab674cbb97cddae8bfda41d8ad51c3', "Your answer is incorrect. Please try again. Are you examining the plot?"
    return(success)

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (122, 2), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['wage', 'when'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['wage', 'when'], msg
    assert round(sum(
        list(answer.wage)
    )) == 2707, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 3, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "1fb672c64fb863655b3da383b19e23a336df5e98", "Your answer is incorrect. Please try again."
    return(success)

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.encoding.color.field.encode('utf8')).hexdigest() == "30603fa9e0f620c305cd627ab0ff138a960c48bd", "Your color is incorrect. Are you setting the correct column to the color channel?"
    assert sha1(answer.encoding.x.aggregate.encode('utf8')).hexdigest() == "09f3246f599ac9a17e658bc0657edea466004792", "Your aggregate function is incorrect. The median function might be useful here?"
    assert sha1(answer.encoding.x.field.encode('utf8')).hexdigest() == "2bf5eebcf9e1dc77882e8b519e2a62ceab49228e", "Your x-axis is incorrect. Are you examining the sample plot correctly?"
    assert not str(answer.encoding.x.scale) == 'Undefined', "Make sure you are specifying a domain range for the x axis, using `alt.Scale() in the x channel."
    assert sha1(str(answer.encoding.x.scale.domain[0]).encode('utf8')).hexdigest() == '1574bddb75c78a6fd2251d61e2993b5146201319', "Make sure that you are specifying the correct domain range for the plot."
    assert sha1(str(answer.encoding.x.scale.domain[1]).encode('utf8')).hexdigest() == 'cb4e5208b4cd87268b208e49452ed6e89a68e0b8', "Make sure that you are specifying the correct domain range for the plot."
    assert sha1(answer.encoding.x.axis.format.encode('utf8')).hexdigest() == "3cdf2936da2fc556bfa533ab1eb59ce710ac80e5", "Your x-axis formatting is incorrect. Are you examining the sample plot correctly?"
    assert sha1(answer.encoding.y.field.encode('utf8')).hexdigest() == "30603fa9e0f620c305cd627ab0ff138a960c48bd", "Your x-axis is incorrect. Are you examining the plot sample correctly?"
    # assert sha1(str(answer.encoding.y.sort).encode('utf8')).hexdigest() == "6274d09f990d0c683058d941dac960d7d39d819a", "Your sorting is incorrect. Are you examining the sample plot correctly?"  
    assert answer.encoding.color.legend is None, "Make sure the plot legend is omitted."
    return(success)

def test_2_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.x.shorthand == 'count()', "Make sure you are encoding the x-axis using the count function."
    return(success)


def test_2_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer.mark.align == 'left', "Make sure you are aligning the text plot left."
    assert answer.mark.baseline == 'middle', "Make sure the baseline for the text plot is in the middle."
    assert answer.mark.dx > 2 or answer2.mark.dx < 8, "Make sure you are setting the dx for the text plot appropriately."
    assert answer.encoding.text.shorthand == 'count()', "Make sure you are encoding the text plot using the count function."
    return(success)

def test_2_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, alt.vegalite.v4.api.VConcatChart), "Make sure you are concatenating both plots using the correct function."
    assert isinstance(answer.vconcat[0], alt.vegalite.v4.api.Chart), "Make sure the median plot is first."
    assert isinstance(answer.vconcat[1], alt.vegalite.v4.api.LayerChart), "Make sure the count plot is second."
    return(success)

def test_2_7_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'tick', "Make sure you are creating a tick plot using the 'mark_tick()' function."
    assert answer.encoding.x.shorthand == 'wage' or answer.encoding.x.field == 'wage', "Make sure you are plotting 'wage' on the x-axis."
    assert answer.encoding.x.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative."
    assert answer.encoding.y.shorthand == 'when' or answer.encoding.y.field == 'when', "Make sure you are plotting 'when' on the y-axis."
    return(success)

def test_2_7_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.x.axis.format == "$", "Make sure you are formatting the x-axis properly."
    assert answer.encoding.color.field == "when", "Make sure you are coloring using the 'when' column."
    assert answer.encoding.color.legend is None, "Make sure your plot does not have a legend."
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    return(success)

def test_2_7_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)


def test_2_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'x').encode('utf8')).hexdigest() == '4a2b94f8a97ab5760cddd2707413b9edfddcae58', "Your answer is incorrect. Please try again. Are you examining the plot?"
    return(success)

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (25, 2), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['Firearm murders', 'Year'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['Firearm murders', 'Year'], msg
    assert round(sum(
        list(answer.iloc[:, 1])
    )) == 6042, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4 or len(answer) == 5 , "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "f1d2bb8869d39e88a14cc27d6ea47c7948b0cbc2" or sha1(str(answer).encode('utf8')).hexdigest() =='9779727f02ead0e8a62579699e7d3d787d79fc9f', "Your answer is incorrect. Please try again."
    return(success)

def test_3_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'area', "Make sure you are generating an area plot using the mark_area() function."
    assert answer.mark.color == '#b0272f', "Make sure you are mapping the colors correctly."
    assert answer.mark.opacity == 0.9, "Make sure you are setting the opacity correctly."
    return(success)

def test_3_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.x.shorthand == 'Year' or answer.encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis."
    assert answer.encoding.y.shorthand == 'Firearm murders' or answer.encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis."
    assert answer.encoding.x.axis.grid == False, "Make sure you are setting grid argument to False in the axis=alt.Axis()."
    assert answer.encoding.y.scale.reverse == True, "Make sure are reversing the scale for the y-axis using alt.Scale()."
    return(success)

def test_3_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    return(success)

def test_3_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer.mark.size == 14 or answer.mark.fontSize == 14, "Make sure you are setting the text size to 14."
    assert answer.mark.color == 'white' or answer.mark.color == '#FFFFFF', "Make sure you are coloring the text white."
    assert answer.mark.dx == 60, "Make sure you are setting the dx for the text plot to 60."
    assert answer.mark.dy == -10, "Make sure you are setting the dx for the text plot to -10."
    assert answer.encoding.x.shorthand == 'Year' or answer.encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis."
    assert answer.encoding.y.shorthand == 'Firearm murders' or answer.encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis."
    assert answer.encoding.text.value == 'Gun law enacted', "make sure you are setting the value of the text appropriately."
    assert list(answer.data.Year) == [1986], "Make sure you are only selecting the year 1986."
    return(success)


def test_3_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining both plots."
    answer.layer[1].mark.type == 'text', "Make sure the second plot is the text plot."
    return(success)

def test_3_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) > 2, "Make sure you are combining the plots."
    assert answer.layer[2].mark.type == 'circle', "Make sure you are creating a scatter plot using the mark_circle() function."
    assert answer.layer[2].mark.color == 'black', "Make sure you are coloring the points black."
    return(success)

def test_3_7_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(list(answer.data.Year)[0], pd._libs.tslibs.timestamps.Timestamp), "Make sure you are parsing the Year column correctly for the area plot."
    assert answer.mark.type == 'area', "Make sure you are generating an area plot using the mark_area() function or the area plot."
    assert answer.mark.color == '#b0272f', "Make sure you are mapping the colors correctly or the area plot."
    assert answer.mark.opacity == 0.9, "Make sure you are setting the opacity correctly or the area plot."
    assert answer.encoding.x.shorthand == 'Year' or answer.encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis or the area plot."
    assert answer.encoding.y.shorthand == 'Firearm murders' or answer.encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis or the area plot."
    assert not "reverse: True" in str(answer.encoding.y), 'Your y-axis should not be reversed.'
    assert answer.encoding.x.axis.grid == False, "Make sure you are setting grid argument to False."
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)


def test_3_7_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.data.shape == (1,2), "Are you filtering your data by Year as a string and not an int?"
    assert isinstance(list(answer.data.Year)[0], pd._libs.tslibs.timestamps.Timestamp), "Make sure you are parsing the Year column correctly or the area plot."
    assert answer.data.iloc[0,1] == 94, "Are you filtering the data to only include the row from 1986? A filtered dataframe should be used as the chart source."
    assert answer.mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer.mark.size == 16 or answer.mark.fontSize ==16, "Make sure you are setting the text size to 16 for the text plot."
    assert answer.mark.color == 'white', "Make sure you are coloring the text white for the text plot."
    assert answer.mark.dx == 60, "Make sure you are setting the dx for the text plot to 60 for the text plot."
    assert answer.mark.dy == 15, "Make sure you are setting the dy for the text plot to 15 for the text plot."
    assert answer.encoding.text.value == 'Gun law enacted', "make sure you are setting the value of the text appropriately for the text plot."
    return(success)


def test_3_7_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'line', "Make sure you are creating a line plot using the mark_line() function."
    assert answer.mark.color == 'black', "Make sure you are coloring the line points black."
    assert answer.mark.opacity == 1.0, "Make sure you are setting the opacity to 1.0 for the line plot."
    return(success)


def test_3_7_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'circle', "Make sure you are creating a scatter plot using the mark_circle() function."
    assert answer.mark.color == 'black', "Make sure you are coloring the scatter points black."
    assert answer.mark.opacity == 1.0, "Make sure you are setting the opacity to 1.0 for the line plot."
    return(success)


def test_3_7_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 4, "Make sure you are combining the plots."
    return(success)


def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'c').encode('utf8')).hexdigest() == '13211ef68928d927b98c56e3497bfbc0a93a377a', "Your answer is incorrect. Please try again. Are you examining the plot?"
    return(success)

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (20, 2), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['the value', 'where'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['the value', 'where'], msg
    assert round(sum(
        list(answer.iloc[:, 1])
    )) == 110, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "b1d5781111d84f7b3fe45a0852e59758cd7a87e5", "Your answer is incorrect. Please try again. Are you examining the dataframe?"
    return(success)

def test_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "9b03c423b7ad8f46a8dc6a4bbd77f5722227e68a", "Your answer is incorrect. Please try again."
    return(success)

def test_4_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'area', "Make sure you are creating a density plot using the mark_area() function."
    assert answer.mark.opacity == 0.4, "Make sure you are setting the opacity correctly."
    assert sorted(answer.transform[0]['as']) == ['density', 'the value'], "Make sure you are naming the new column as density"
    assert answer.transform[0]['groupby'] == ['where'], "Make sure you are grouping by the correct column."
    return(success)


def test_4_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    assert 'Ocean waves' in str(answer.title), 'Makes sure you are giving the plot a title of "Ocean waves" (careful of spaces and capitalization).'
    return(success)


def test_4_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.x.shorthand == 'the value' or answer.encoding.x.field == 'the value', "Make sure you are plotting 'the value' on the x-axis."
    assert answer.encoding.y.shorthand == 'density' or answer.encoding.y.field == 'density', "Make sure you are plotting 'density' on the y-axis."
    assert answer.encoding.x.axis.format == "s", "Make sure you are formatting the x-axis to 's'."
    assert answer.encoding.color.field == "where", "Make sure you are coloring using the 'where' column."
    return(success)


def test_4_4_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    if 'legend' in answer.config.to_dict().keys():
        assert answer.config.to_dict()['legend']['orient'] == 'top', ""
        assert answer.config.to_dict()['legend']['title'] == None, "Make sure your plot does not have a legend title."
    elif 'legend' in answer.encoding.color.to_dict().keys():
        assert answer.encoding.color.legend.title is None, "Make sure your plot does not have a legend title."
        assert answer.encoding.color.legend.orient == 'top', "Make sure you are putting the legend in the correct place."
    else: 
        raise Exception("Are you sure you are formatting your legend using '.configure_legend()' or encoding it in the color channel using 'alt.Legend()'?")
    assert sorted(answer.encoding.color.scale.range) == ['aquamarine', 'steelblue'], "Make sure you are setting the range of the colors correctly."
    return(success)


def test_4_4_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.config.axis.grid == False, "Make sure you are setting the axis grid correctly."
    assert answer.config.view.strokeWidth == 0, "Make sure you are setting the stroke width correctly."
    return(success)

def test_4_6_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'point', "Make sure you are creating a point plot 'mark_point()' function."
    assert answer.mark.size == 50, "Make sure you are setting the point size correctly."
    assert answer.encoding.x.shorthand == 'the value' or answer.encoding.x.field == 'the value', "Make sure you are plotting 'the value' on the x-axis."
    assert answer.encoding.y.shorthand == 'where' or answer.encoding.y.field == 'where', "Make sure you are plotting 'where' on the y-axis."
    return(success)

def test_4_6_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(answer.config) == 'Undefined', "To change the font size of your axis and labels, you should be using the method '.configure_axis()'."
    assert answer.config.axis.labelFontSize == 12, "Make sure you are setting the axis font size correctly."
    assert answer.config.axis.titleFontSize == 12, "Make sure you are setting the title font size correctly."
    return(success)

def test_4_6_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.title.text)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    assert not str(type(answer.title.subtitle[0])) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a subtitle for your plot."
    assert not answer.title.subtitle[0].islower(), "Make sure the plot title is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot title does not contain underscores."
    return(success)

def test_4_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'e').encode('utf8')).hexdigest() == '1f444844b1ca616009c2b0e3564fecc065872b5b', "Your answer is incorrect. Please try again. Are you examining the plot?"
    return(success)
