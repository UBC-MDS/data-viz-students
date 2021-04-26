from hashlib import sha1
import pandas as pd
import pytest
import altair
import sys
import numpy as np
import re
import altair as alt

success = "Success"

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

def test_1_2_new(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "e92ae78645e9479d96660fa380bd379dbafc94b5", "Your answer is incorrect. Please try again."
    return(success)

def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 5, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "7a475469311b4cc276c05507d630bad34d28a13a", "Your answer is incorrect. Please try again."
    return(success)


def test_1_3(answer):
    assert sha1(answer.mark.color.encode('utf8')).hexdigest() == "bc74f4f071a5a33f00ab88a6d6385b5e6638b86c", "The color is incorrect. Are you examining the original plot correctly?"
    assert sha1(str(answer.mark.size).encode('utf8')).hexdigest() == "310b86e0b62b828562fc91c7be5380a992b2786a", "The points szie is incorrect. Are you examining the original plot correctly?"
    assert sha1(answer.mark.type.encode('utf8')).hexdigest() == "00b7b8118efde44c546b69243ec15b21cd64c9d9", "The plot type is incorrect. Are you examining the plot original correctly?"
    assert sha1(answer.encoding.x.field.encode('utf8')).hexdigest() == "09ade1377f03dadec1de00aaa6fd4ac215edac2c", "Your x-axis is incorect. Are you examining the original plot correctly?"
    assert sha1(answer.encoding.y.field.encode('utf8')).hexdigest() == "02cd3b107a9c91476522398de1fd67d78fffb72d", "Your y-axis is incorect. Are you examining the original plot correctly?"
    assert sha1(answer.title.text.strip().encode('utf8')).hexdigest() == "a14a9d1b06af5f02ce76873ddb919e1d0ec5c62f", "Your plot title is incorrect. Are you examining the original plot correctly?"
    assert sha1(answer.title.subtitle.strip().encode('utf8')).hexdigest() == "8effba3e3a11d79e3352f8889e0f9069d4368702", "Your plot subtitle is incorrect. Are you examining the original plot correctly?"
    return(success)

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'rect', "Make sure you are creating a 2D histogram plot using the 'mark_rect()' function."
    assert answer.encoding.x.bin.maxbins == 30, "Make sure you are setting the maxbins on the x-axis to 30"
    assert answer.encoding.y.bin.maxbins == 30, "Make sure you are setting the maxbins on the y-axis to 30"
    assert answer.encoding.y.bin.extent == (0, 1), "Make sure you are setting the bin extent between (0, 1)"
    assert answer.encoding.x.shorthand == 'dissatisfaction_last_year' or answer.encoding.x.field == 'dissatisfaction_last_year', "Make sure you are plotting 'dissatisfaction_last_year' on the x-axis."
    assert answer.encoding.x.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative"
    assert answer.encoding.y.shorthand == 'dissatisfaction_this_year' or answer.encoding.y.field == 'dissatisfaction_this_year', "Make sure you are plotting 'dissatisfaction_this_year' on the y-axis."
    assert answer.encoding.y.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative"
    assert not answer.encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not answer.encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores"
    assert not answer.encoding.x.title is None, "Make sure you are providing a title for your X-axis"
    assert not answer.encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert not answer.title.text is None, "Make sure you are providng a title for your plot"
    assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores"
    assert not answer.title.subtitle[0] is None, "Make sure you are providng a title for your plot"
    assert not answer.title.subtitle[0].islower(), "Make sure the plot title is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot title does not contain underscores"
    assert answer.encoding.color.aggregate == 'count', "Make sure you are coloring by count."
    return(success)

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 't').encode('utf8')).hexdigest() == '589e942e00a7dd64a273deb5041c7ce469f2bad7', "Your answer is incorrect. Please try again. Are you examing the plot?"
    return(success)

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'p').encode('utf8')).hexdigest() == '0691a664b24b6f15b20cd5aee64b72271db08be1', "Your answer is incorrect. Please try again. Are you examing the plot?"
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
    assert sha1(str(answer.encoding.x.scale.domain).encode('utf8')).hexdigest() == "d5e2a943d04efce547862f94d68e954999b19dbc", "The domain is incorrect. Are you examining the sample plot correctly?"
    assert sha1(answer.encoding.x.axis.format.encode('utf8')).hexdigest() == "3cdf2936da2fc556bfa533ab1eb59ce710ac80e5", "Your x-axis formatting is incorrect. Are you examining the sample plot correctly?"
    assert sha1(answer.encoding.y.field.encode('utf8')).hexdigest() == "30603fa9e0f620c305cd627ab0ff138a960c48bd", "Your x-axis is incorrect. Are you examining the plot sample correctly?"
    # assert sha1(str(answer.encoding.y.sort).encode('utf8')).hexdigest() == "6274d09f990d0c683058d941dac960d7d39d819a", "Your sorting is incorrect. Are you examining the sample plot correctly?"  
    assert answer.encoding.color.legend is None, "Make sure the plot legend is omitted."
    return(success)

def test_2_4(answer1, answer2):
    assert not answer1 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer1.encoding.x.shorthand == 'count()', "Make sure you are ecoding the x-axis using the count function."
    assert answer2.mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer2.mark.align == 'left', "Make sure you are aligning the text plot left."
    assert answer2.mark.baseline == 'middle', "Make sure the baseline for the text plot is in the middle."
    assert answer2.mark.dx > 2 or answer2.mark.dx < 8, "Make sure you are setting the dx for the text plot appropriately."
    assert answer2.encoding.text.shorthand == 'count()', "Make sure you are ecoding the text plot using the count function."
    return(success)

def test_2_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, alt.vegalite.v4.api.VConcatChart), "Make sure you are concatenating both plots."
    assert isinstance(answer.vconcat[0], altair.vegalite.v4.api.Chart), "Make sure the median plot is first"
    assert isinstance(answer.vconcat[1], alt.vegalite.v4.api.LayerChart), "Make sure the count plot is second"
    return(success)

def test_2_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'tick', "Make sure you are creating a tick plot using the 'mark_tick()' function."
    assert answer.encoding.x.shorthand == 'wage' or answer.encoding.x.field == 'wage', "Make sure you are plotting 'wage' on the x-axis."
    assert answer.encoding.x.type == 'quantitative', "Make sure you are specifying the x-axis as quantitative"
    assert answer.encoding.y.shorthand == 'when' or answer.encoding.y.field == 'when', "Make sure you are plotting 'when' on the y-axis."
    assert answer.encoding.x.axis.format == "$", "Make sure you are formatting the x-axis properly."
    assert answer.encoding.color.field == "when", "Make sure you are coloring using the 'when' column."
    assert answer.encoding.color.legend is None, "Make sure your plot does not have a legend"
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    assert not answer.encoding.x.title is None, "Make sure you are providing a title for your X-axis"
    assert not answer.encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert not answer.title is None, "Make sure you are providng a title for your plot"
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores"
    return(success)

def test_2_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'x').encode('utf8')).hexdigest() == '4a2b94f8a97ab5760cddd2707413b9edfddcae58', "Your answer is incorrect. Please try again. Are you examing the plot?"
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
    assert len(answer) == 4, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "f1d2bb8869d39e88a14cc27d6ea47c7948b0cbc2", "Your answer is incorrect. Please try again."
    return(success)

def test_3_3(answer):
    assert answer.mark.type == 'area', "Make sure you are generating an area plot using the mark_area() function."
    assert answer.mark.color == '#b0272f', "Make sure you are mapping the colors correctly."
    assert answer.mark.opacity == 0.9, "Make sure you are setting the opacity correctly."
    assert answer.encoding.x.shorthand == 'Year' or answer.encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis."
    assert answer.encoding.y.shorthand == 'Firearm murders' or answer.encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis."
    assert answer.encoding.x.axis.grid == False, "Make sure you are setting grid argument to False in the axis=alt.Axis()."
    assert answer.encoding.y.scale.reverse == True, "Make sure are reversing the scale for the y-axis using alt.Scale()."
    assert not answer.encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not answer.encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores"
    return(success)

def test_3_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining both plots."
    answer = answer.layer[1]
    assert answer.mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer.mark.size == 14, "Make sure you are setting the text size to 14."
    assert answer.mark.color == 'white' or answer.mark.color == '#FFFFFF', "Make sure you are coloring the text white"
    assert answer.mark.dx == 60, "Make sure you are setting the dx for the text plot to 60."
    assert answer.mark.dy == -10, "Make sure you are setting the dx for the text plot to -10."
    assert answer.encoding.x.shorthand == 'Year' or answer.encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis."
    assert answer.encoding.y.shorthand == 'Firearm murders' or answer.encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis."
    assert answer.encoding.text.value == 'Gun law enacted', "make sure you are setting the value of the text appropriately"
    assert list(answer.data.Year) == [1986], "Make sure you are only selecting the year 1986"
    return(success)

def test_3_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) > 2, "Make sure you are combining the plots"
    assert answer.layer[2].mark.type == 'circle', "Make sure you are creating a scatter plot using the mark_circle() function."
    assert answer.layer[2].mark.color == 'black', "Make sure you are coloring the points black."
    return(success)

def test_3_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 4, "Make sure you are combining the plots"
    assert isinstance(list(answer.data.Year)[0], pd._libs.tslibs.timestamps.Timestamp), "Make sure you are parsing the Year column correctly or the area plot."
    assert answer.layer[0].mark.type == 'area', "Make sure you are generating an area plot using the mark_area() function or the area plot."
    assert answer.layer[0].mark.color == '#b0272f', "Make sure you are mapping the colors correctly or the area plot."
    assert answer.layer[0].mark.opacity == 0.9, "Make sure you are setting the opacity correctly or the area plot."
    assert answer.layer[0].encoding.x.shorthand == 'Year' or answer.layer[0].encoding.x.field == 'Year', "Make sure you are plotting 'Year' on the x-axis or the area plot."
    assert answer.layer[0].encoding.y.shorthand == 'Firearm murders' or answer.layer[0].encoding.y.field == 'Firearm murders', "Make sure you are plotting Firearm murders on the y-axis or the area plot."
    assert answer.layer[0].encoding.x.axis.grid == False, "Make sure you are setting grid argument to False."
    assert not answer.layer[0].title is None, "Make sure you are providing a title for the area plot"
    assert not answer.layer[0].title.islower(), "Make sure the area plot title is capitalized."
    assert answer.layer[0].title.count("_") == 0, "Make sure your area plot title does not contain underscores."
    assert answer.layer[3].mark.type == 'text', "Make sure you are creating a text plot using the mark_text() function."
    assert answer.layer[3].mark.size == 16, "Make sure you are setting the text size to 16 for the text plot."
    assert answer.layer[3].mark.color == 'white', "Make sure you are coloring the text white for the text plot."
    assert answer.layer[3].mark.dx == 60, "Make sure you are setting the dx for the text plot to 60 for the text plot."
    assert answer.layer[3].mark.dy == 15, "Make sure you are setting the dx for the text plot to 15 for the text plot."
    assert answer.layer[3].encoding.text.value == 'Gun law enacted', "make sure you are setting the value of the text appropriately for the text plot"
    assert answer.layer[2].mark.type == 'circle', "Make sure you are creating a scatter plot using the mark_circle() function."
    assert answer.layer[2].mark.color == 'black', "Make sure you are coloring the scatter points black."
    assert answer.layer[2].mark.opacity == 1.0, "Make sure you are setting the opacity to 1.0 for the scatter plot"
    assert answer.layer[1].mark.type == 'line', "Make sure you are creating a line plot using the mark_line() function."
    assert answer.layer[1].mark.color == 'black', "Make sure you are coloring the line points black."
    assert answer.layer[1].mark.opacity == 1.0, "Make sure you are setting the opacity to 1.0 for the line plot"
    return(success)

def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'c').encode('utf8')).hexdigest() == '13211ef68928d927b98c56e3497bfbc0a93a377a', "Your answer is incorrect. Please try again. Are you examing the plot?"
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
    assert sha1(str(answer).encode('utf8')).hexdigest() == "b1d5781111d84f7b3fe45a0852e59758cd7a87e5", "Your answer is incorrect. Please try again. Are you examing the dataframe?"
    return(success)

def test_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "9b03c423b7ad8f46a8dc6a4bbd77f5722227e68a", "Your answer is incorrect. Please try again."
    return(success)

def test_4_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'area', "Make sure you are creating a density plot using the mark_area() function."
    assert answer.mark.opacity == 0.4, "Make sure you are setting the opacity correctly."
    assert sorted(answer.transform[0]['as']) == ['density', 'the value'], "Make sure you are naming the new column as density"
    assert answer.transform[0]['groupby'] == ['where'], "Make sure you are grouping by the correct column."
    assert not answer.title is None, "Make sure you are providing a title for your Y-axis"
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    assert answer.title.count("_") == 0, "Make sure your title does not contain underscores"
    assert answer.encoding.x.shorthand == 'the value' or answer.encoding.x.field == 'the value', "Make sure you are plotting 'the value' on the x-axis."
    assert answer.encoding.y.shorthand == 'density' or answer.encoding.y.field == 'density', "Make sure you are plotting 'density' on the y-axis."
    assert answer.encoding.x.axis.format == "s", "Make sure you are formatting the x-axis to 's'."
    assert answer.encoding.color.field == "where", "Make sure you are coloring using the 'where' column."
    assert answer.encoding.color.legend.title is None, "Make sure your plot does not have a legend"
    assert answer.encoding.color.legend.orient == 'top', "Make sure you are putting the legend in the correct place."
    assert sorted(answer.encoding.color.scale.range) == ['aquamarine', 'steelblue'], "Make sure you are setting the range of the colors correctly."
    assert answer.config.axis.grid == False, "Make sure you are setting the axis grid correctly."
    assert answer.config.view.strokeWidth == 0, "Make sure you are setting the stroke width correctly"
    return(success)

def test_4_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'point', "Make sure you are creating a point plot 'mark_point()' function."
    assert answer.mark.size == 50, "Make sure you are setting the point size correctly."
    assert answer.encoding.x.shorthand == 'the value' or answer.encoding.x.field == 'the value', "Make sure you are plotting 'the value' on the x-axis."
    assert answer.encoding.y.shorthand == 'where' or answer.encoding.y.field == 'where', "Make sure you are plotting 'where' on the y-axis."
    assert not answer.encoding.x.title is None, "Make sure you are providing a title for your X-axis"
    assert not answer.encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert not answer.title.text is None, "Make sure you are providng a title for your plot"
    assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores"
    assert not answer.title.subtitle[0] is None, "Make sure you are providng a title for your plot"
    assert not answer.title.subtitle[0].islower(), "Make sure the plot title is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot title does not contain underscores"
    assert answer.config.axis.labelFontSize == 12, "Make sure you are setting the axis font size correctly."
    assert answer.config.axis.titleFontSize == 12, "Make sure you are setting the title font size correctly."
    return(success)

def test_4_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'e').encode('utf8')).hexdigest() == '1f444844b1ca616009c2b0e3564fecc065872b5b', "Your answer is incorrect. Please try again. Are you examing the plot?"
    return(success)
