from hashlib import sha1
import pandas as pd
import pytest
import altair as alt
import sys
import numpy as np

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


def test_0_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (17, 8), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['continent', 'distinct_syllables', 'id', 'information_density', 'iso_lang', 'language', 'lat', 'lon'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['continent', 'distinct_syllables', 'id', 'information_density', 'iso_lang', 'language', 'lat', 'lon'], msg
    assert round(sum(
        list(answer.information_density)
    )) == 102, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert round(sum(
        list(answer.distinct_syllables)
    )) == 50980, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_0_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, pd.core.frame.DataFrame), "Make sure your answer is of type dataframe."
    assert answer.shape == (1, 8), "The dimensions of your answer is incorrect. Are you filtering correctly?"
    assert sha1(str(list(answer.distinct_syllables)[0]).encode('utf8')).hexdigest() == '403f0fe6fbadbfff9f9133475034f7ee11d65e4c', "Some values in your solution is incorrect. Are you filtering correctly?"
    assert sha1(str(list(answer.continent)[0]).encode('utf8')).hexdigest() == '576347ec826f38428d8c8a6f8ec4acb2bceab911', "Some values in your solution is incorrect. Are you filtering correctly?"
    assert sha1(str(answer).lower().encode('utf8')).hexdigest() == "d1ed60ea8074d9221eaf3dc762fb9e9d6e526fc4", "Your answer is incorrect. Please try again. The max function might be useful here."
    return(success)


def test_1_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.mark.size == 50, "Make sure you are setting the size of the points correctly."
    assert answer.encoding.x.shorthand == 'information_density' or answer.encoding.x.field == 'information_density', "Make sure you are plotting 'information_density' on the x-axis."
    assert answer.encoding.x.type  == 'quantitative', "Make sure the x-axis is of type 'quantitative'."
    assert answer.encoding.y.type  == 'quantitative', "Make sure the y-axis is of type 'quantitative'."
    assert answer.encoding.y.shorthand == 'distinct_syllables' or answer.encoding.y.field == 'distinct_syllables', "Make sure you are plotting 'distinct_syllables' on the y-axis."
    assert 'zero: False' in str(answer.encoding.x), "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert 'zero: False' in str(answer.encoding.y),"Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    assert answer.encoding.y.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    return(success)

def test_1_1_2(answer):
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    assert isinstance(answer.title, alt.utils.schemapi.UndefinedType), "Make sure your plot does NOT have a title this time."
    return(success)


def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.mark.size == 50, "Make sure you are setting the size of the points correctly."
    assert answer.encoding.color.field == 'continent', "Make sure you are coloring the points by 'continent."
    assert answer.encoding.x.shorthand == 'information_density' or answer.encoding.x.field == 'information_density', "Make sure you are plotting 'information_density' on the x-axis."
    assert answer.encoding.y.shorthand == 'distinct_syllables' or answer.encoding.y.field == 'distinct_syllables', "Make sure you are plotting 'distinct_syllables' on the y-axis."
    assert answer.encoding.x.type  == 'quantitative', "Make sure the x-axis is of type 'quantitative'."
    assert answer.encoding.y.type  == 'quantitative', "Make sure the y-axis is of type 'quantitative'."
    assert 'zero: False' in str(answer.encoding.x), "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert 'zero: False' in str(answer.encoding.y),"Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    assert answer.encoding.y.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    assert not str(type(answer.encoding.y.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your y-axis."
    assert answer.encoding.y.title.count("_") == 0, "Make sure your y-axis title does not contain underscores."
    assert not answer.encoding.y.title.islower(), "Make sure the plot y-axis title is capitalized."
    return(success)


def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, pd.core.frame.DataFrame), "Make sure your answer is of type dataframe."
    assert answer.shape == (1, 8), "The dimensions of your answer is incorrect. Are you filtering correctly?"
    assert sha1(str(list(answer.distinct_syllables)[0]).encode('utf8')).hexdigest() == '4a934273b8b55e10bc9ef5b13eae098792114786', "Some values in your solution is incorrect. Are you filtering correctly?"
    assert sha1(str(list(answer.continent)[0]).encode('utf8')).hexdigest() == '576347ec826f38428d8c8a6f8ec4acb2bceab911', "Some values in your solution is incorrect. Are you filtering correctly?"
    assert sha1(str(answer).lower().encode('utf8')).hexdigest() == "7cad205a263199ed028a094c0bcc75be2d286c70", "Your answer is incorrect. Please try again. Are you filtering correctly?"
    return(success)

def test_1_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'text', "Make sure you are creating a text plot for the second plot using the mark_text() function."
    assert sha1(str(answer.data).lower().encode('utf8')).hexdigest() == "7cad205a263199ed028a094c0bcc75be2d286c70", "Make sure you are using the correct data for the text plot."
    assert answer.encoding.x.shorthand == 'information_density' or answer.encoding.x.field == 'information_density', "Make sure you are plotting 'information_density' on the x-axis for the text plot."
    assert answer.encoding.y.shorthand == 'distinct_syllables' or answer.encoding.y.field == 'distinct_syllables', "Make sure you are plotting 'distinct_syllables' on the y-axis for the text plot."
    if 'field' in answer.encoding.text.to_dict().keys():
        assert answer.encoding.text.field == 'language', "Make sure you are setting the text to 'language' for the text plot."
    elif 'value' in answer.encoding.text.to_dict().keys(): 
        assert answer.encoding.text.value == 'French', "Make sure you are setting the text value equal to 'French' for the text plot."
    else:
        raise Exception('Are you encoding the text channel properly?')
    return(success)   


def test_1_5_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining the scatter plot with the text plot."
    assert not str(type(answer.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your plot."
    assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
    assert not answer.title.islower(), "Make sure the plot title is capitalized."
    return(success)

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining the colored plot with the text plot"
    answer2 = answer.layer[1]
    assert answer2.mark.type == 'text', "Make sure you are creating a text plot for the second plot using the mark_text() function."
    assert sha1(str(answer2.data).lower().encode('utf8')).hexdigest() == "7cad205a263199ed028a094c0bcc75be2d286c70", "Make sure you are using the correct data for the text plot."
    assert answer2.encoding.x.shorthand == 'information_density' or answer2.encoding.x.field == 'information_density', "Make sure you are plotting 'information_density' on the x-axis for the text plot."
    assert answer2.encoding.y.shorthand == 'distinct_syllables' or answer2.encoding.y.field == 'distinct_syllables', "Make sure you are plotting 'distinct_syllables' on the y-axis for the text plot."
    assert answer2.encoding.text.field == 'language' or answer2.encoding.text.field == 'language', "Make sure you are setting the text to 'language' for the text plot."
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)


def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    case1 = (sha1(str(answer[0]).encode("utf8")).hexdigest() ==
             "042dc4512fa3d391c5170cf3aa61e6a638f84342")
    case2 = (sha1(str(answer[1]).encode("utf8")).hexdigest() ==
             "3918373cf5559c54b52c7066428f6c4118d31c23")
    case3 = (sha1(str(answer[2]).encode("utf8")).hexdigest() ==
             "425ffc1422dc4f32528bd9fd5af355fdb5c96192")
    case4 = (sha1(str(answer[3]).encode("utf8")).hexdigest() ==
             "7a38d8cbd20d9932ba948efaa364bb62651d5ad4")
    total_sum = sum([
        case1, case2, case3, case4
    ])
    assert total_sum == 4, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 4 - total_sum)
    return(success)

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (2288, 7), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['age', 'duration', 'iso_lang', 'sex', 'speaker', 'syllables', 'text'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['age', 'duration', 'iso_lang', 'sex', 'speaker', 'syllables', 'text'], msg
    assert round(sum(
        list(answer.duration)
    )) == 35219, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert round(sum(
        list(answer.syllables)
    )) == 231536, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (2288, 8), "Your dataframe dimensions are incorrect. Are you adding the extra column?"
    assert 'speech_rate' in list(answer.columns), "Make sure you are adding the 'speech_rate' column to your dataframe."
    assert round(sum(
        list(answer.speech_rate)
    )) == 15172, "The values for speech_rate is incorrect. Are you computing them correctly?"
    return(success)

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (17, 2), "Your dataframe dimensions are incorrect. Are you computing the mean for each country?"
    assert 'speech_rate' in list(answer.columns), "Make sure you are computing the mean 'speech_rate' for each country."
    assert round(max(answer.speech_rate), 2) == 8.03, "The max speech rate is incorrect. Are you taking the mean of the speech_rate column?"
    assert round(min(answer.speech_rate), 2) == 4.7, "The min speech rate is incorrect. Are you taking the mean of the speech_rate column?"
    return(success)

def test_2_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (17, 9), "Your dataframe dimensions are incorrect. Are you computing the mean for each country?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['continent', 'distinct_syllables', 'id', 'information_density', 'iso_lang', 'language', 'lat', 'lon', 'speech_rate'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns)) == ['continent', 'distinct_syllables', 'id', 'information_density', 'iso_lang', 'language', 'lat', 'lon', 'speech_rate'], msg
    assert round(max(answer.speech_rate),2) == 8.03, "The max speech rate is incorrect. Are you taking the mean?"
    assert round(min(answer.speech_rate),2) == 4.7, "The min speech rate is incorrect. Are you taking the mean?"
    assert round(sum(
        list(answer.information_density)
    )) == 102, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert round(sum(
        list(answer.distinct_syllables)
    )) == 50980, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return(success)

def test_2_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'circle', "Make sure you are creating a scatter plot using the 'mark_circle()' function."
    assert answer.mark.size == 50, "Make sure you are setting the size of the points correctly."
    assert answer.encoding.color.field == 'continent' or answer.encoding.color.shorthand == 'continent', "Make sure you are coloring the points by 'continent."
    assert answer.encoding.color.type  == 'nominal', "Make sure the color is of type 'nominal'."
    assert answer.encoding.x.shorthand == 'information_density' or answer.encoding.x.field == 'information_density', "Make sure you are plotting 'information_density' on the x-axis."
    assert answer.encoding.y.shorthand == 'speech_rate' or answer.encoding.y.field == 'speech_rate', "Make sure you are plotting 'speech_rate' on the y-axis."
    assert answer.encoding.x.type  == 'quantitative', "Make sure the x-axis is of type 'quantitative'."
    assert answer.encoding.y.type  == 'quantitative', "Make sure the y-axis is of type 'quantitative'."
    return(success)

def test_2_5_2(answer):
    assert 'zero: False' in str(answer.encoding.x), "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert 'zero: False' in str(answer.encoding.y),"Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    assert answer.encoding.y.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the y-axis."
    return(success)


def test_2_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 3, "The length of your answer is incorrect."
    case1 = (sha1(str(answer[0]).encode("utf8")).hexdigest() ==
             "3918373cf5559c54b52c7066428f6c4118d31c23")
    case2 = (sha1(str(answer[1]).encode("utf8")).hexdigest() ==
             "425ffc1422dc4f32528bd9fd5af355fdb5c96192")
    case3 = (sha1(str(answer[2]).encode("utf8")).hexdigest() ==
             "2b946ddae90df50f553375cbadede63ef5dcc8b0")
    total_sum = sum([
        case1, case2, case3
    ])
    assert total_sum == 3, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 3 - total_sum)
    return(success)

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (2288, 14), "Your dataframe dimensions are incorrect. Are you merging the correct dataframes?"
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['age', 'continent', 'duration', 'id', 'information_density'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns))[0:5] == ['age', 'continent', 'duration', 'id', 'information_density'], msg
    assert round(max(answer.speech_rate),2) == 9.49, "The max speech rate is incorrect. Are you merging correctly?"
    assert round(min(answer.speech_rate),2) == 3.59, "The min speech rate is incorrect. Are you merging correctly?"
    assert round(max(answer.age),2) == 69, "The max age is incorrect. Are you merging correctly?"
    assert round(min(answer.age),2) == 16, "The min age is incorrect. Are you merging correctly"
    return(success)

def test_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (2288, 15), "Your dataframe dimensions are incorrect. Are you adding the extra column?"
    assert 'information_rate' in list(answer.columns), "Make sure you are adding the 'information_rate' column to your dataframe."
    assert round(sum(
        list(answer.information_rate)
    )) == 89582, "The values for information_rate is incorrect. Are you computing them correctly?"
    return(success)

def test_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, pd.core.series.Series), "Make sure your solution is of type Pandas series."
    assert len(list(answer)) == 17, "The length of your answer is incorrect. Are you taking the mean?"
    assert list(answer) == sorted(answer), "Make sure you are sorting the mean values."
    assert round(max(list(answer)),2) == 45.93, "Are you taking the mean? Some values are incorrect."
    assert round(min(list(answer)),2) == 33.8, "Are you taking the mean? Some values are incorrect."
    return(success)

def test_3_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == 'tick', "Make sure you are creating a rug plot using the 'mark_tick()' function."
    assert answer.mark.size == 10, "Make sure you are setting the size of the points correctly."
    assert answer.mark.opacity == 0.3, "Make sure you are setting the opacity correctly."
    return(success)

def test_3_4_2(answer):
    assert answer.encoding.color.field == 'continent' or answer.encoding.color.shorthand == 'continent', "Make sure you are coloring the points by 'continent."
    assert answer.encoding.color.type  == 'nominal', "Make sure the color is of type 'nominal'."
    assert answer.encoding.x.shorthand == 'information_rate' or answer.encoding.x.field == 'information_rate', "Make sure you are plotting 'information_rate' on the x-axis."
    assert answer.encoding.y.shorthand == 'language' or answer.encoding.y.field == 'language', "Make sure you are plotting 'language' on the y-axis."
    assert answer.encoding.x.type  == 'quantitative', "Make sure the x-axis is of type 'quantitative'."
    assert answer.encoding.y.type  == 'nominal', "Make sure the y-axis is of type 'nominal'."
    assert 'zero: False' in str(answer.encoding.x), "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    assert answer.encoding.x.scale.zero == False, "Make sure you are using the 'alt.Scale(zero=False)' for the x-axis."
    return(success)


def test_3_4_3(answer):
    temp = answer.encoding.y.sort
    temp = [x.lower() for x in temp]
    assert sha1(str(temp).encode('utf8')).hexdigest() == 'e4887296c24c55da7e9febd00b89cae188a68b71', "Make sure you are sorting the y-axis correctly"
    assert not str(type(answer.encoding.x.title)) == "<class 'altair.utils.schemapi.UndefinedType'>", "Make sure you are providing a title for your x-axis."
    assert answer.encoding.x.title.count("_") == 0, "Make sure your x-axis title does not contain underscores."
    assert not answer.encoding.x.title.islower(), "Make sure the plot x-axis title is capitalized."
    return(success)


def test_3_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining the colored plot with the text plot."
    answer2 = answer.layer[1]
    assert answer2.mark.type == 'circle', "Make sure you are creating a scatter plot for the second plot using the mark_circle() function."
    assert answer2.mark.size == 40, "Make sure you are setting the size of the points on the second plot correctly."
    return(success)

def test_3_5_2(answer):
    answer2 = answer.layer[1]
    assert answer2.encoding.x.shorthand == 'information_rate' or answer2.encoding.x.field == 'information_rate', "Make sure you are plotting 'information_rate' on the x-axis for the text plot."
    assert answer2.encoding.x.type  == 'quantitative', "Make sure the x-axis is of type 'quantitative' for the text plot."
    assert answer2.encoding.x.aggregate == 'mean', "Make sure you are taking the mean of the information_rate for the second plot."
    assert answer2.encoding.y.sort == ['Thai', 'Hungarian', 'Cantonese', 'Basque','German', 'Turkish', 'Italian', 'Catalan',
                                       'Serbian', 'Finnish', 'Korean','Japanese','Mandarin', 'Spanish', 'Vietnamese', 'English',
                                       'French'], "Make sure that you are plotting the mean information rate in ascending order." 
    assert answer2.encoding.color.value == 'black', "Make sure you are coloring the points black."
    return(success)

def test_3_5_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)

def test_3_6_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == '32f897f04b545b8da26e1e2ebac7eeb732b0cbb1', "Your answer for the european continent is incorrect. Are you analyzing the plot carefully?"
    return(success)

def test_3_7_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == 'b269a8528451c93b142881721c2b29922aeede70', "Your answer for the european continent is incorrect. Are you analyzing the plot carefully?"
    return(success)

def test_3_7_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == 'e71223abaadfe7c7d69b345880e88a73c5a6d122', "Your answer for the asian continent is incorrect. Are you analyzing the plot carefully?"
    return(success)

def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + 'k').lower().encode('utf8')).hexdigest() == "4273aaeff3593ced0804d5f350c1a1c59d55a7f5", "Your answer is incorrect. Please try again. Are you examining the range of values on the plot?"
    return(success)

def test_3_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + 'p').lower().encode('utf8')).hexdigest() == "ac78b022715c5b8357b4dca8045e8463b4de2124", "Your answer is incorrect. Please try again. Think about how the points vary in the plot?"
    return(success)

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.format.feature == 'countries', "Make sure you are extracting the correct feature from the world data."
    assert answer.url == "https://vega.github.io/vega-datasets/data/world-110m.json" or answer.url == "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/world-110m.json", "Make sure you are using the correct URL."
    return(success)

def test_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (16, 10), "Your dataframe dimensions are incorrect. Are you grouping by the correct variables and taking the mean? You may have to reset your index if you have not done so."
    msg = "Your dataframe contains the incorrect columns. Are you reading in the correct dataframe? \
    \nExpected ['age', 'duration', 'id', 'information_density', 'information_rate'], but got {0}".format(
        sorted(list(answer.columns)))
    assert sorted(list(answer.columns))[0:5] == ['age', 'duration', 'id', 'information_density', 'information_rate'], msg
    assert round(max(answer.speech_rate),2) == 8.03, "The max speech rate is incorrect. Are you grouping by the correct variables and taking the mean?"
    assert round(min(answer.speech_rate),2) == 4.7, "The min speech rate is incorrect. Are you grouping by the correct variables and taking the mean?"
    assert round(max(answer.lon),2) == 138.25, "The max value for lon is incorrect. Are you grouping by the correct variables and taking the mean?"
    assert round(min(answer.lon),2) == -3.75, "The min value for lon is incorrect. Are you grouping by the correct variables and taking the mean?"
    return(success)

def test_4_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.data.url == 'https://vega.github.io/vega-datasets/data/world-110m.json' or answer.data.url == 'https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/world-110m.json', 'Make sure you are using the correct data source.'
    assert len(answer.layer) == 2, "Make sure you are combining both plots."
    c2 = answer.layer[1]
    assert c2.mark.type == 'geoshape', 'Make sure the mark is of type geoshape.'
    assert sha1(c2.encoding.color.field.encode('utf8')).hexdigest() == '5430f4cf21194d437aee6e85dacdc28df35513f5', "Make sure you are coloring the map properly."
    return(success)

def test_4_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    c2 = answer.layer[1]
    assert not str(c2.encoding.color.scale.scheme) == 'Undefined', "Make sure that you are setting the scheme of the color scale."
    assert c2.encoding.tooltip[0].field == 'language', "Make sure that you are filling 'language' in for the first tooltip field." 
    assert c2.encoding.tooltip[1].field == 'information_rate', "Make sure that you are filling 'information_rate' in for the second tooltip field."
    #assert sha1(c2.encoding.color.scale.scheme.encode('utf8')).hexdigest() == "f04893b5d78f49439d4b872d6dd942ff839a2978", "Make sure you are setting the scheme of the color scale properly." #we can rewrite this to do what we want later.
    assert sha1(c2.encoding.tooltip[0]['field'].encode('utf8')).hexdigest() == "e11523c5ff23fc1600aca2d8ee5adb542c5ce4b3" or sha1(c2.encoding.tooltip[0]['shorthand'].encode('utf8')).hexdigest() == "e11523c5ff23fc1600aca2d8ee5adb542c5ce4b3", "Make sure you are setting the tooltip correctly."
    assert sha1(c2.encoding.tooltip[1]['field'].encode('utf8')).hexdigest() == "5430f4cf21194d437aee6e85dacdc28df35513f5" or sha1(c2.encoding.tooltip[1]['shorthand'].encode('utf8')).hexdigest() == "5430f4cf21194d437aee6e85dacdc28df35513f5", "Make sure you are setting the tooltip correctly."
    return(success)


def test_4_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    c2 = answer.layer[1]
    assert sha1(str(answer.projection.scale).encode('utf8')).hexdigest() == "9f9af029585ba014e07cd3910ca976cf56160616", "Make sure you are setting the projection scale correctly."
    assert answer.projection.type == 'naturalEarth1', "Make sure you are setting the projection to 'naturalEarth1'."
    assert answer.projection.translate[0] == 120, "Make sure you are translating by 120 in position 0."
    assert answer.projection.translate[1] == 260, "Make sure you are translating by 260 in position 1."
    return(success)


def test_4_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.layer) == 2, "Make sure you are combining both plots."
    c1 = answer.layer[0]
    assert sha1(c1.mark.type.encode('utf8')).hexdigest() == 'e665a0a6727c7f21ac16366012fc73bcafff2d6a', "Make sure you are using the correct mark function."
    return(success)

def test_4_5_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    c2 = answer.layer[1]
    assert sha1(c2.encoding.latitude.field.encode('utf8')).hexdigest() == 'f1bd09c12f53c4adc7135f87451af543ec79a43d' or sha1(c2.encoding.latitude.shorthand.encode('utf8')).hexdigest() == 'f1bd09c12f53c4adc7135f87451af543ec79a43d', "Make sure you are assigning the latitude correctly."
    assert sha1(c2.encoding.longitude.field.encode('utf8')).hexdigest() == '7c8c8b6917b098e739038a18ed3e75c4f92de9e1'or sha1(c2.encoding.longitude.shorthand.encode('utf8')).hexdigest() == '7c8c8b6917b098e739038a18ed3e75c4f92de9e1', "Make sure you are assigning the longitude correctly."
    assert sha1(c2.encoding.size.field.encode('utf8')).hexdigest() == 'd047746b5ced84e37578c24bf7470a5ea1d27cb6' or sha1(c2.encoding.size.field.encode('utf8')).hexdigest() == 'd047746b5ced84e37578c24bf7470a5ea1d27cb6', "Make sure you are setting the size correctly."
    return(success)

def test_4_5_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    c1 = answer.layer[0]
    c2 = answer.layer[1]
    assert sha1(c2.encoding.tooltip[0]['field'].encode('utf8')).hexdigest() == 'e11523c5ff23fc1600aca2d8ee5adb542c5ce4b3' or sha1(c2.encoding.tooltip[0]['field'].encode('utf8')).hexdigest() == 'e11523c5ff23fc1600aca2d8ee5adb542c5ce4b3', "Make sure you are setting the tooltip correctly."
    assert sha1(c2.encoding.tooltip[1]['field'].encode('utf8')).hexdigest() == 'd047746b5ced84e37578c24bf7470a5ea1d27cb6' or sha1(c2.encoding.tooltip[1]['field'].encode('utf8')).hexdigest() == 'd047746b5ced84e37578c24bf7470a5ea1d27cb6', "Make sure you are setting the tooltip correctly."
    assert sha1(answer.projection.type.encode('utf8')).hexdigest() == 'c097995793f4d6151d79e94af2fd76fc46a3e006', "Make sure you are setting the projection type correctly."
    assert sha1(str(answer.projection.translate).encode('utf8')).hexdigest() == '210bc26a0bb8c78a606ad5428e37f27f3a903b63', "Make sure you are zooming and panning the plot correctly"
    return(success)

def test_4_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'm').encode('utf8')).hexdigest() == "a47109ee9df5886f4fc3501e447706767399b93d", "Your answer is incorrect. Please try again. What is easier to intepret? Points or gradients?"
    return(success)

def test_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer.hconcat) == 2, "Make sure you are combining both plots."
    c1 = answer.hconcat[0]
    c2 = answer.hconcat[1]
    assert len(c1.layer) == 2, "Make sure you are setting the annotated plot first"
    assert c1.layer[0].encoding.x.shorthand == 'information_density' or c1.layer[0].encoding.x.field == 'information_density', "Make sure you are setting the annotated plot first."
    assert c2.encoding.x.shorthand == 'information_density' or c2.encoding.x.field == 'information_density', "Make sure you are setting the info rate plot second."
    assert c2.encoding.y.shorthand == 'speech_rate' or c2.encoding.y.field == 'speech_rate', "Make sure you are setting the info rate plot second."
    if 'middle' in str(answer.config):
        assert answer.config.title.anchor == 'middle', " Make sure you are anchoring the title in the middle."
    elif 'middle' in str(answer.title.anchor): 
        assert answer.title.anchor == 'middle', " Make sure you are anchoring the title in the middle."
    else:
        raise Exception("Are you anchoring your title in the middle of the plot?")
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    return(success)

def test_5_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert 'vconcat' in list(dir(answer)) or 'hconcat' in list(dir(answer)), "Make sure you are concatening the plots horizontally and vertically."
    if 'vconcat' in list(dir(answer)):
        assert len(answer.vconcat) >= 2, "Make sure you are concatenating at least two of the plots vertically."
    else:
        assert len(answer.hconcat) >= 2, "Make sure you are concatenating at least two of the plots horizontally."
    return(success)

def test_5_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    if 'middle' in str(answer.config):
        assert answer.config.title.anchor == 'middle', " Make sure you are anchoring the title in the middle."
    elif 'middle' in str(answer.title.anchor): 
        assert answer.title.anchor == 'middle', " Make sure you are anchoring the title in the middle."
    else:
        raise Exception("Are you anchoring your title in the middle of the plot?")
    return(success)

def test_5_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    if type(answer.title) == str:
        assert answer.title.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.islower(), "Make sure the plot title is capitalized."
    elif isinstance(answer.title, alt.vegalite.v4.schema.core.TitleParams):
        assert answer.title.text.count("_") == 0, "Make sure your plot title does not contain underscores."
        assert not answer.title.text.islower(), "Make sure the plot title is capitalized."
    else: 
        raise Exception("Are you sure you are assigning a title to your plot?")
    assert not answer.title.subtitle[0] is None, "Make sure you are providing a subtitle for your plot"
    assert not answer.title.subtitle[0].islower(), "Make sure the plot subtitle is capitalized."
    assert answer.title.subtitle[0].count("_") == 0, "Make sure your plot subtitle does not contain underscores."
    return(success)

def test_5_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == "756b96224c2ebac45a561fd2d9144308ffa4afbe", "Your answer is incorrect. Please try again. How well does the claims in the narrative you have chosen match with the plots?"
    return(success)

def test_6_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    case1 = (sha1(str(answer[0]).encode("utf8")).hexdigest() ==
             "042dc4512fa3d391c5170cf3aa61e6a638f84342")
    case2 = (sha1(str(answer[1]).encode("utf8")).hexdigest() ==
             "3918373cf5559c54b52c7066428f6c4118d31c23")
    case3 = (sha1(str(answer[2]).encode("utf8")).hexdigest() ==
             "7a38d8cbd20d9932ba948efaa364bb62651d5ad4")
    case4 = (sha1(str(answer[3]).encode("utf8")).hexdigest() ==
             "833da188871dde4c49e08271ff3deff524b7992c")
    total_sum = sum([
        case1, case2, case3, case4
    ])
    assert total_sum == 4, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 4 - total_sum)
    return(success)

def test_6_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, list), "Make sure your answer is of type list."
    answer = [x.lower() for x in sorted(answer)]
    assert len(answer) == 4, "The length of your answer is incorrect."
    case1 = (sha1(str(answer[0]).encode("utf8")).hexdigest() ==
             "042dc4512fa3d391c5170cf3aa61e6a638f84342")
    case2 = (sha1(str(answer[1]).encode("utf8")).hexdigest() ==
             "2b946ddae90df50f553375cbadede63ef5dcc8b0")
    case3 = (sha1(str(answer[2]).encode("utf8")).hexdigest() ==
             "7a38d8cbd20d9932ba948efaa364bb62651d5ad4")
    case4 = (sha1(str(answer[3]).encode("utf8")).hexdigest() ==
             "833da188871dde4c49e08271ff3deff524b7992c")
    total_sum = sum([
        case1, case2, case3, case4
    ])
    assert total_sum == 4, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 4 - total_sum)
    return(success)
