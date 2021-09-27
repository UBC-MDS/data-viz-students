from hashlib import sha1
import pandas as pd
import pytest
import altair
import sys
import numpy as np
import re

success = "Success"

def test_titles(answer):
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)


def test_main_title(answer):
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a main title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success) 


def test_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (1008, 9), "Your dataframe dimensions are incorrect. Are you using the 'read_json' function?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['budget', 'id', 'runtime', 'title'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns)[0:4]) == ['budget', 'id', 'runtime', 'title'], msg
    assert "Finding Nemo" in list(
        answer.title
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.runtime)
    ) == 113081, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.bin.maxbins == 40, "Make sure you are setting the max number of bins to 40."
    assert answer.encoding.y.aggregate == 'count', "Make sure you are plotting the count on the y-axis."
    assert answer.encoding.x.shorthand == 'vote_average' or answer.encoding.x.field == 'vote_average', "Make sure you are plotting 'vote_average' on the y-axis."
    return(success)

def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'm').encode('utf8')).hexdigest() == 'a67acd6e68f872b807a1c9afe3a2453564e57877', "Your answer is incorrect. Please try again. What information does a density plot provide?"
    return(success)

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 5, "The length of your answer is incorrect"
    assert sha1(str(answer).encode('utf8')).hexdigest() == 'd27eb999a6fd98dbe856fb3b8350bed6026b6a6c', "Your answer is incorrect. The dtypes function might be useful here."
    return(success)

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.spec.encoding.x.bin.maxbins == 40,"Make sure you are setting the maxbins to 40."
    assert answer.spec.encoding.x.field.repeat == 'repeat', "Make sure you are using the 'repeat' argument."
    assert answer.spec.encoding.y.aggregate == 'count', "Make sure you are plotting the count on the Y-axis."
    assert answer.spec.height == 150, "Make sure you are setting a height of 150."
    assert answer.spec.width == 250, "Make sure you are setting a width of 250."
    assert answer.columns == 2, "Make sure you are specifying two columns."
    return(success)

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "fd1286353570c5703799ba76999323b7c7447b06", "Your answer is incorrect, please try again."
    return(success)

def test_1_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'l').encode('utf8')).hexdigest() == 'ef3ecccf258fa062c5c6521a4887d40541963af7', "Your answer is incorrect. Please try again. What is the shape of the curve? Which way is it leaning?"
    return(success)

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.spec.encoding.x.field.repeat == 'column', "Make sure you are using the 'repeat' argument on the columns."
    assert answer.spec.encoding.y.shorthand == 'vote_average' or answer.spec.encoding.y.field == 'vote_average', "Make sure you are plotting 'vote_average' on the y-axis."
    assert 'repeat": {\n    "column":' in answer.to_json(), "Make sure you are setting a parameter of 'column' in the repeat function." 
    assert answer.spec.height == 120, "Make sure you are setting a height of 120."
    assert answer.spec.width == 120, "Make sure you are setting a width of 120."
    return(success)

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.spec.encoding.x.field.repeat == 'column', "Make sure you are passing the columns to the repeat argument."
    assert answer.spec.encoding.y.field.repeat == 'row', "Make sure you are passing the rows to the repeat argument."
    assert answer.spec.height == 80, "Make sure you are setting a height of 80."
    assert answer.spec.width == 80, "Make sure you are setting a width of 80."
    assert 'repeat": {\n    "column":' in answer.to_json(), "Make sure you are setting a parameter of 'column' in the repeat function." 
    assert ' "row": [' in answer.to_json(), "Make sure you are setting a parameter of 'row' in the repeat function."     
    return(success)

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark.type == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.spec.mark.opacity == 0.5, "Make sure you are setting the opcaity to 0.5."
    assert answer.spec.mark.size == 10, "Make sure you are setting the size of the points to 10."
    assert answer.spec.encoding.x.field.repeat == 'column', "Make sure you are passing the columns to the repeat argument."
    assert answer.spec.encoding.y.field.repeat == 'row', "Make sure you are passing the rows to the repeat argument."
    assert answer.spec.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    assert answer.spec.encoding.y.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the y axis."
    assert answer.spec.height == 120, "Make sure you are setting a height of 120."
    assert answer.spec.width == 120, "Make sure you are setting a width of 120."
    assert not str(answer.spec.encoding.x.axis) == 'Axis({\n  labels: False\n})', "Instead of removing the axes labels in the x channel, use the method 'configure_axis()' as specified in the question."
    assert not str(answer.spec.encoding.y.axis) == 'Axis({\n  labels: False\n})', "Instead of removing the axes labels in the y channel, use the method 'configure_axis()' as specified in the question."
    assert not str(answer.config) == 'Undefined', "Make sure that you are removing the axis labels using 'configure_axis'."
    assert answer.config.axis.labels == False, "Make sure you are removing the axis labels."
    return(success)

def test_2_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    t1 = answer.encoding.x.shorthand == 'level_0' or answer.encoding.x.field == 'level_0'
    t2 = answer.encoding.y.shorthand == 'level_1' or answer.encoding.y.field == 'level_1'
    t3 = answer.encoding.x.shorthand == 'level_1' or answer.encoding.x.field == 'level_1'
    t4 = answer.encoding.y.shorthand == 'level_0' or answer.encoding.y.field == 'level_0'
    assert t1 or t3, "Make sure you are plotting 'level_0' or 'level_1' on the x-axis."
    assert t2 or t4, "Make sure you are plotting 'level_0' or 'level_1' on the y-axis."
    return(success)

def test_2_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [x.lower() for x in answer]
    assert sha1(str(sorted(answer)).encode('utf8')).hexdigest() == "aad49a7dea2183f089132e33a2995a438882760e", "Your answers are incorrect. Please try again. Which circle has the biggest size and darkest color?"
    return(success)

def test_2_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'rect', "Make sure you are creating a 2D histogram plot using the 'mark_rect()' function."
    assert answer.spec.encoding.x.bin.maxbins == 25, "Make sure you are setting the maxbins on the x-axis to 25."
    assert answer.spec.encoding.y.bin.maxbins == 25, "Make sure you are setting the maxbins on the y-axis to 25."
    assert answer.spec.encoding.x.field.repeat == 'column', "Make sure you are passing the columns to the repeat argument."
    assert answer.spec.encoding.y.field.repeat == 'row', "Make sure you are passing the rows to the repeat argument."
    assert answer.spec.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    assert answer.spec.encoding.y.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the y axis."
    assert answer.spec.encoding.color.aggregate == 'count', "Make sure you are encoding the color channel to count."
    assert answer.spec.height == 120, "Make sure you are setting a height of 120."
    assert answer.spec.width == 120, "Make sure you are setting a width of 120."
    assert answer.config.axis.labels == False, "Make sure you are removing the axis labels."
    return(success)

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (1669, 9), "Your dataframe dimensions are incorrect. Are you using the 'explode' function on genres?"
    msg = "Your dataframe contains the incorrect columns. Do you have the correct dataframe? \
    \nExpected ['budget', 'id', 'runtime', 'title'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns)[0:4]) == ['budget', 'id', 'runtime', 'title'], msg
    assert len(set(answer.genres)) == 9, "The number of movie genres is incorrect. Do you have the correct dataframe?"
    assert list(answer.genres).count("Animation") == 115, "The number of 'Animation' movies is incorrect. Are you using the 'explode' function on genres?"
    assert list(answer.genres).count("Horror") == 96, "The number of 'Horror' movies is incorrect. Are you using the 'explode' function on genres?"
    return(success)

def test_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'boxplot', "Make sure you are creating a box plot using the 'mark_boxplot()' function."
    assert answer.spec.encoding.x.field.repeat == 'repeat', "Make sure you are using the 'repeat' argument."
    assert answer.spec.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    assert answer.spec.encoding.y.shorthand == 'genres' or answer.spec.encoding.y.field == 'genres', "Make sure you are plotting 'genres' on the y-axis."
    assert not answer.spec.encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not answer.spec.encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert answer.spec.encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores"
    assert answer.spec.height == 200, "Make sure you are setting a height of 200."
    assert answer.spec.width == 360, "Make sure you are setting a width of 360."
    assert answer.columns == 2, "Make sure you are specifying two columns."
    return(success)

def test_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "66f79d8a6327c82c9033e6d65ff03322a3766c87", "Your answer is incorrect. Which genre has it's box furthest to the right?"
    return(success)

def test_3_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "a6b8b600c27ce95ddcf867cfc503564c89fe816a", "Your answer is incorrect. Which genre has it's box furthest to the right?"
    return(success)

def test_3_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "99f8b5ec55efbdab33c3cf5f9723ed37726c7047", "Your answer is incorrect. Which genre has the most number of points above the box?"
    return(success)

def test_3_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (1078, 9), "Your dataframe dimensions are incorrect. Are you using the 'explode' function on the studios column?"
    msg = "Your dataframe contains the incorrect columns. Do you have the correct dataframe? \
    \nExpected ['budget', 'id', 'runtime', 'title'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns)[0:4]) == ['budget', 'id', 'runtime', 'title'], msg
    assert len(set(answer.studios)) == 11, "The number of movie studios is incorrect. Do you have the correct dataframe?"
    assert list(answer.studios).count("Marvel Studios") == 15, "The number of 'Marvel Studios movies is incorrect. Are you using the 'explode' function on the studios column?"
    assert list(answer.studios).count("Canal+") == 72, "The number of 'Canal+' movies is incorrect. Are you using the 'explode' function on the studios column?"
    return(success)

def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.spec.mark == 'boxplot', "Make sure you are creating a box plot using the 'mark_boxplot()' function."
    assert answer.spec.encoding.x.field.repeat == 'repeat', "Make sure you are using the 'repeat' argument."
    assert answer.spec.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x axis."
    assert answer.spec.encoding.y.shorthand == 'studios' or answer.spec.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    assert not answer.spec.encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not answer.spec.encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert answer.spec.encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores."
    assert answer.spec.height == 200, "Make sure you are setting a height of 200."
    assert answer.spec.width == 320, "Make sure you are setting a width of 360."
    assert answer.columns == 2, "Make sure you are specifying two columns."
    return(success)

def test_3_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "18a94e532f79c9ce14acabcc3daabed529e486c3", "Your answer is incorrect. Which studio has it's box furthest to the left?"
    return(success)

def test_3_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "f70ea671e99773c063ce308454eb6286b302e444", "Your answer is incorrect. Which studio has the largest bar length in the plot?"
    return(success)  

def test_3_11(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "89082fdeb11d0c2c7d3ea6782d28a1ff06eeaa9f", "Your answer is incorrect. Which studio has the smalles bar?"
    return(success)  

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (1802, 9), "Your dataframe dimensions are incorrect. Are you using the 'explode' function on genres?"
    msg = "Your dataframe contains the incorrect columns. Do you have the correct dataframe? \
    \nExpected ['budget', 'id', 'runtime', 'title'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns)[0:4]) == ['budget', 'id', 'runtime', 'title'], msg
    assert len(set(answer.genres)) == 9, "The number of movie genres is incorrect. Do you have the correct dataframe?"
    assert list(answer.genres).count("Animation") == 139, "The number of 'Animation' movies is incorrect. Are you using the 'explode' function on genres?"
    assert list(answer.genres).count("Horror") == 96, "The number of 'Horror' movies is incorrect. Are you using the 'explode' function on genres?"
    return(success)

def test_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'rect', "Make sure you are generating a heatmap using the mark_rect function."
    assert answer.encoding.color.aggregate == 'count', "Make sure you are coloring by the count aggregate."
    assert answer.encoding.x.shorthand == 'genres' or answer.encoding.x.field == 'genres', "Make sure you are plotting 'genres' on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    return(success)

def test_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'square', "Make sure you are generating a heatmap using the mark_square function."
    assert answer.encoding.color.aggregate == 'count', "Make sure you are coloring by the count aggregate."
    assert answer.encoding.size.aggregate == 'count', "Make sure you are setting the size by the count aggregate."
    assert answer.encoding.x.shorthand == 'genres' or answer.encoding.x.field == 'genres', "Make sure you are plotting 'genres' on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    return(success)

def test_4_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 3, "The length of your answer is incorrect"
    assert sha1(str(answer).encode('utf8')).hexdigest() == '0d6bf5a69a9d02468294e3e8e984068a146b7659', "Your answer is incorrect. Are you examining the number of shaded regions on the plot for Marvel Studios?"
    return(success) 

def test_4_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, int), "Make sure your answer is of type integer."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "1b6453892473a467d07372d45eb05abc2031647a", "Your answer is incorrect. Please try again. Are you examing the plots carefully?"
    return(success)

def test_4_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "63b12989474b64a1b1f8c2035d6ef2a4640845c6", "Your answer is incorrect, please try again."
    return(success)

def test_4_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(re.sub('[.!@#$]', '', answer).lower().encode('utf8')).hexdigest() == "64ad577207c3fe433812973e9fddefc16292d8f2", "Your answer is incorrect, please try again. Which studio has the largest square in the action column?"
    return(success)

def test_4_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [re.sub('[.!@#$]', '', x).lower() for x in sorted(answer)]
    assert len(answer) == 2, "The length of your answer is incorrect"
    assert sha1(str(answer).encode('utf8')).hexdigest() == '404c470afdfecbaec45d6cbd7934752e4e150d31', "Your answer is incorrect. Are you examing the plots carefully?"
    return(success) 

def test_4_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'circle', "Make sure you are generating a heatmap using the mark_circle function."
    assert answer.encoding.color.field == 'proportion', "Make sure you are setting the size by proportions."
    assert answer.encoding.size.field == 'proportion', "Make sure you are coloring by proportions."
    assert answer.encoding.x.shorthand == 'genres' or answer.encoding.x.field == 'genres', "Make sure you are plotting 'genres' on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    return(success)

def test_4_11(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 1, "The length of your answer is incorrect"
    assert sha1(str(answer).encode('utf8')).hexdigest() == '84fc310e9a0706cd16257836c8546cf61b85cd99', "Your answer is incorrect. Which studio has the most shaded regions?"
    return(success)
