from hashlib import sha1
import pandas as pd
import pytest
import altair
import sys
import numpy as np

success = "Success"
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
    assert isinstance(answer, int), "Make sure your answer is of type integer."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "Your answer is incorrect. Please try again. Are you observing the dataframe carefully?"
    return(success)

def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (11, 9), "Your dataframe dimensions are incorrect. Are you using the 'describe' function?"
    msg = "Your dataframe contains the incorrect columns. Do you have the correct dataframe? \
    \nExpected ['budget', 'id', 'runtime', 'title'], but got {0}".format(
        sorted(list(answer.columns))[0:4])
    assert sorted(list(answer.columns)[0:4]) == ['budget', 'id', 'runtime', 'title'], msg
    assert answer["id"].isna().sum() == 3, "Your dataframe contains incorrect values. Are you using the 'include = all' argument?"
    assert answer.iloc[0].sum() == 9072.0, "Your dataframe contains incorrect values. Are you using the 'include = all' argument?"
    return(success)

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, int) or isinstance(answer, np.int64), "Make sure your answer is of type integer."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "e3cbba8883fe746c6e35783c9404b4bc0c7ee9eb", "Your answer is incorrect. Please try again. The unique function might be useful here."
    return(success)

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, float) or isinstance(answer, np.int64), "Make sure your answer is of type float."
    assert sha1(str(float(answer)).encode('utf8')).hexdigest() == "16bd07eb063ed8d91d0441a30162786853bbf11c", "Your answer is incorrect. Please try again."
    return(success)

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, np.int64) or isinstance(answer, np.int), "Make sure your answer is of type int."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "b3c0730cf3f50613e40561e67c871fdb92820cf9", "Your answer is incorrect. Please try again. The 'freq' argument might be useful here."
    return(success)

def test_1_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer == round(answer,2), "Make sure you are rounding to two decimal places."
    assert isinstance(answer, float), "Make sure your answer is of type float."
    assert sha1(str(answer).encode('utf8')).hexdigest() == "8e687e9d91738ea9b2adea35617e089188a8750a", "Your answer is incorrect. Please try again."
    return(success)

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    assert answer.encoding.y.sort == 'x' or answer.encoding.y.sort == 'x', "Make sure you are sorting the y-axis based on x-axis values."
    assert not answer.encoding.y.title is None, "Make sure you are providing a title for your y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.x.title is None, "Make sure you are providing a title for your x-axis."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert answer.height == 800, "Make sure the height of your plot is 800."
    assert answer.width == 600, "Make sure the width of your plot is 600."
    return (success)

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 2, "The number of answers is incorrect. There should be two studios."
    assert sha1(answer[0].encode('utf8')).hexdigest() == 'c900823aecf9bf4310374b1a95c94a1d4bc46acf', "One of the studios is incorrect. Please try again."
    assert sha1(answer[1].encode('utf8')).hexdigest() == '319f4042005f1f023d666dddfa5741f95fb0eb41', "One of the studios is incorrect. Please try again."
    return(success)

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert "collaboration" in list(answer.columns), "Make sure you are creating the 'collaboration' column."
    assert list(answer.collaboration).count(True) == 68, "The number of collaborations is incorrect. Are you counting correctly?"
    assert set(answer.collaboration) == {False, True}, "Your collaboration column contains incorrect values. Make sure it is either 'True' or 'False'."
    return(success)

def test_2_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.y.shorthand == 'collaboration' or answer.encoding.y.field == 'collaboration', "Make sure you are plotting 'collaboration' on the y-axis."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert answer.height == 300, "Make sure the width of your plot is 800"
    assert answer.width == 300, "Make sure the width of your plot is 600"
    return (success)

def test_2_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.bin.maxbins == 50, "Make sure you are setting the max number of bins to 50"
    assert answer.encoding.x.shorthand == 'revenue' or answer.encoding.x.field == 'revenue', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_2_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + "m").encode('utf8')).hexdigest() == "e283e1df945bccf5e009169e7d9f4115c9de7f05", "Your answer is incorrect. Please try again."
    return(success)

def test_2_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.facet.shorthand == 'collaboration' or answer.facet.field == 'collaboration', "Make sure the plot is faceted based on 'collaboration'."
    return ("Success")

def test_2_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.resolve.scale.y == 'independent', "Make sure you are scaling the y-axis independently for each facet."
    return(success)

def test_2_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + "w").encode('utf8')).hexdigest() == "e2c44c572970480e0089da2b6ef90adce84d30fd", "Your answer is incorrect. Please try again."
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
    sha1(str(answer).encode('utf8')).hexdigest() == "0ade7c2cf97f75d009975f4d720d1fa6c19f4897", "The number of movie genres is incorrect. Make sure you are taking the unique ones."
    assert sha1(str([x.lower() for x in sorted(answer)]).encode('utf8')).hexdigest() == 'd1e18eccc02419fdb9712cad011e39cb52f53591', "Your movie genres are incorrect. Please try again."
    return(success)

def test_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 9, "The length of your answer is incorrect"
    assert sha1(str(answer).encode('utf8')).hexdigest() == 'd1e18eccc02419fdb9712cad011e39cb52f53591', "Your answer is incorrect. Make sure you are sorting by median gross income."
    return(success)

def test_3_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'boxplot' or answer.mark.type == 'boxplot', "Make sure you are creating a boxplot using the 'mark.boxplot()' function."
    assert answer.encoding.x.shorthand == 'revenue' or answer.encoding.x.field == 'revenue', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.shorthand == 'genres' or answer.encoding.y.field == 'genres', "Make sure you are plotting 'genres' on the y-axis."
    assert sha1(str([x.lower() for x in answer.encoding.y.sort]).encode('utf8')).hexdigest() == '0a74024851e27e1ddec77854b01cac1991aef8e3', "Make sure you are sorting the plot by median gross income."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_3_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [round(x) for x in list(answer)]
    assert max(answer) == 2579946310, "The maximum 99.9 quantile value is incorrect. Are you computing these properly?"
    assert min(answer) == 518735868, "The minimum 99.9 quantile value is incorrect. Are you computing these properly?"
    return(success)

def test_3_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    sha1((answer.lower()).encode('utf8')).hexdigest() == '9c3bb49ffea1144231cbe02d904b8d9018744e9d', "The science fiction outlier is incorrect. Are you filtering correctly?"
    return(success)

def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.y.shorthand == 'genres' or answer.encoding.y.field == 'genres', "Make sure you are plotting 'genres' on the y-axis."
    assert answer.encoding.y.sort == 'x' or answer.encoding.y.sort == 'x', "Make sure you are sorting the y-axis based on x-axis values"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return (success)

def test_3_9(answer):
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

def test_3_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar' , "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    assert answer.encoding.y.sort == 'x' or answer.encoding.y.sort == 'x', "Make sure you are sorting the y-axis based on x-axis values."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return (success)

def test_3_11(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 11, "Make sure you are sorting all the available studios."
    assert sha1(str([x.lower() for x in answer]).encode('utf8')).hexdigest() == 'd11c50387780c87be9e5541d8819274d27251a11', "The order is incorrect. Are you sorting by revenue?"
    return(success)

def test_3_12(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'boxplot' or answer.mark.type == 'boxplot', "Make sure you are creating a boxplot using the 'mark.boxplot()' function."
    assert answer.encoding.x.shorthand == 'revenue' or answer.encoding.x.field == 'revenue', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.shorthand == 'studios' or answer.encoding.y.field == 'studios', "Make sure you are plotting 'studios' on the y-axis."
    assert sha1(str([x.lower() for x in answer.encoding.y.sort]).encode('utf8')).hexdigest() == 'd11c50387780c87be9e5541d8819274d27251a11', "Make sure you are sorting the plot by revenue."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_3_13(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == 'c900823aecf9bf4310374b1a95c94a1d4bc46acf', "The studio with the highest revenue is incorrect. Are you plotting correctly?"
    return(success)

def test_3_14(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == 'f70ea671e99773c063ce308454eb6286b302e444', "The studio which is the most unpredictable is incorrect. Are you plotting correctly?"
    return(success)

def test_3_15(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower()).encode('utf8')).hexdigest() == '18a94e532f79c9ce14acabcc3daabed529e486c3', "The studio with the highest median is incorrect. Are you plotting correctly?"
    return(success)

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'tick' or answer.mark.type == 'tick', "Make sure you are creating a rug plot using the 'mark_tick()' function."
    assert answer.mark.opacity == 0.5, "Make sure you are setting the opacity to 0.5."
    assert answer.encoding.color.field == 'revenue_size' or answer.encoding.color.shorthand == 'revenue_size', "Make sure you are colouring by 'revenue_size'."
    assert answer.encoding.x.shorthand == 'vote_average' or answer.encoding.x.field == 'vote_average', "Make sure you are plotting 'vote_average' on the x-axis."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.color.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a proper title for the colour channel."
    assert not answer.encoding.color.title.islower(), "Make sure the plot colour legend title is capitalized."
    assert answer.encoding.color.title.count("_") == 0, "Make sure the title for the colour does not contain underscores."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for the plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return (success)

def test_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark == 'bar' or answer.mark.type == 'bar', "Make sure you are creating a bar plot using the 'mark_bar()' function."
    assert answer.encoding.x.bin.maxbins == 30, "Make sure you are setting the max number of bins to 30."
    assert answer.encoding.x.shorthand == 'vote_average' or answer.encoding.x.field == 'vote_average', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.color.shorthand == 'revenue_size' or answer.encoding.color.field == 'revenue_size', "Make sure you are colouring by 'revenue_size'."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.encoding.color.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a proper title for the colour channel."
    assert answer.encoding.color.title.count("_") == 0, "Make sure the title for the colour does not contain underscores."
    assert not answer.encoding.color.title.islower(), "Make sure the plot colour legend title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providng a title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_4_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.encoding.y.stack is None or  answer.encoding.y.stack == False, "Make sure you are setting the 'stack' argument to appropriately."
    assert answer.encoding.x.bin.maxbins == 30, "Make sure you are setting the max number of bins to 30."
    assert answer.encoding.x.shorthand == 'vote_average' or answer.encoding.x.field == 'vote_average', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.aggregate == 'count', "Make sure you are plotting the count on the x-axis."
    assert answer.encoding.color.shorthand == 'revenue_size' or answer.encoding.color.field == 'revenue_size', "Make sure you are colouring by 'revenue_size'."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_4_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert "revenue_size" in str(answer.transform), "Make sure you are grouping by 'revenue_size'."
    assert "vote_average" in str(answer.transform), "Make sure you are computing the density values using the 'vote_average' column."
    assert "density_vals" in str(answer.transform), "Make sure you are giving a name of 'density_vals' to the KDE estimates."
    assert answer.mark.opacity == 0.5, "Make sure you are setting the opacity to 0.5."
    assert answer.mark.type == 'area', "Make sure you are creating a density plot using the 'mark_area()' function."
    assert answer.encoding.x.shorthand == 'vote_average' or answer.encoding.x.field == 'vote_average', "Make sure you are plotting 'revenue' on the x-axis."
    assert answer.encoding.y.shorthand == 'density_vals' or answer.encoding.y.field == 'density_vals', "Make sure you are plotting 'density_vals' on the y-axis."
    assert answer.encoding.color.shorthand == 'revenue_size' or answer.encoding.color.field == 'revenue_size', "Make sure you are colouring by 'revenue_size'."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providng a title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_4_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.facet.shorthand == 'revenue_size' or answer.facet.field == 'revenue_size', "Make sure the plot is faceted based on 'revenue_size'."
    assert answer.columns == 1, "Make sure you are faceting into a single column."
    return (success)

def test_4_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + "l").encode('utf8')).hexdigest() == "f55fb78160b93a5368e129ce16f85548eb77df5f", "Your answer is incorrect. Please try again."
    return(success)
