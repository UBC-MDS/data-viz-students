from hashlib import sha1
import pandas as pd
import pytest
import altair as alt
import sys


# Disable maximum number of rows restriction
alt.data_transformers.disable_max_rows()

def test_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'd').encode('utf8')).hexdigest() != '388ad1c312a488ee9e12998fe097f2258fa8d5ee', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 'd').encode('utf8')).hexdigest() == '85dde59bec27686708dc612f174dee372e89513b', "Your answer is incorrect. You can refer to the video at around 00:50 mark."
    return("Success")

def test_1_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() in ['c3508cc85df617843e2018b9a81ec09e8c09fd25', '554436ee3311dbbb133a88a83b99f47f04f94753'], "Your answer is incorrect. You can refer to the video at around 01:40 mark."
    return("Success")

def test_1_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'a').encode('utf8')).hexdigest() != '1c42c72cf95aa1b76609b585b34baf6b501d713e', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 'a').encode('utf8')).hexdigest() == 'cb3ded381b0c06eef3712a90851650e9eaa0b341', "Your answer is incorrect. You can refer to the video at around 02:00 mark."
    return("Success")

def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 't').encode('utf8')).hexdigest() != '27e90dfa57c358acfaf470860f6f72c9282ce995', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 't').encode('utf8')).hexdigest() == '0855009c46728a5c8cb9aa53860e3b38d932c17a', "Your answer is incorrect. You can refer to the video at around 03:35 mark."
    return("Success")

def test_1_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == list, "Your answer is incorrect. Please make sure your answer is a list of upper case letter(s)."
    assert len(answer) == 2, "Your answer is incorrect. Hint: There are 2 correct answers."
    # sort the list and concatenate into a string before checking answer
    assert sha1("".join(sorted(map(str.upper, answer))).encode('utf8')).hexdigest() == '0f4d56d1e20778bf2e1052ecb3219509238fb660', "Your answer is incorrect. You can refer to the video at around 04:00 - 04:50 mark."
    return("Success")

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() in ['79be276817ebcd106b9fc3d227e18059faf7790e', '50696dbfb6619de36774115f2378ad6e4491dd26', '2b1acadd26fe202d5a082e0f5164cb0f8aae14cc'], "Your answer is incorrect. You can refer to the video at around 07:53 mark."
    return("Success")

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'a').encode('utf8')).hexdigest() != '6c0596b8ac609191181a90517d51c0b486f23799', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 'a').encode('utf8')).hexdigest() == '2fd22ce656b849cb086889e5eacd1da49228eb0a', "Your answer is incorrect. You can refer to the video at around 09:20 mark."
    return("Success")

def test_1_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'v').encode('utf8')).hexdigest() != '1fd5892de3702847cdc183f23de8aff67b99a319', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 'v').encode('utf8')).hexdigest() == 'f62d7c52b60e11c098c129afa29f635600a6466a', "Your answer is incorrect. You can refer to the video at around 10:20 - 11:30 mark."
    return("Success")

def test_1_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer != "", "Please add your reflection and make sure you're not passing an empty string."
    assert len(answer.split(" ")) >= 5, "Please make sure your reflection is at least 5 words long. We want to make sure you have a chance to think about the effectiveness of appropriate visualization choices!"
    return("Success")

def test_2_1b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.dtypes['year'] in ['<M8[ns]', '>M8[ns]', 'datetime64[ns]'], "Please make sure the 'year' column is parsed correctly using parse_dates argument."
    return("Success")

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer == (38982, 14), "Your answer is incorrect. Please make sure you are passing the shape of gapminder_df as a tuple."
    return("Success")

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 178, "Your answer has incorrect number of rows. Please make sure you are filtering for only the observations from year 1962."
    assert answer.shape[1] == 14, "Your answer has incorrect number of columns. Please make sure you are returning the same number of columns as original dataframe"
    assert set(answer['year']) == {pd.Timestamp('1962-01-01 00:00:00')}, "Your answer is incorrect. Please make sure the 'year' column is of type datetime and you are filtering for only the observations from year 1962."
    return("Success")

def test_2_4a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert answer.mark == 'circle', "Make sure you are using the correct mark type."
    return("Success")

def test_2_4b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert (answer.encoding.x.shorthand in {'children_per_woman', 'children_per_woman:quantitative', 'children_per_woman:Q'} or 
            answer.encoding.x.field in {'children_per_woman', 'children_per_woman:quantitative', 'children_per_woman:Q'}), "Make sure you are using 'children_per_woman' as the x-axis encoding."
    assert (answer.encoding.y.shorthand in {'life_expectancy', 'life_expectancy:quantitative', 'life_expectancy:Q'} or 
            answer.encoding.y.field in {'life_expectancy', 'life_expectancy:quantitative', 'life_expectancy:Q'}), "Make sure you are using 'life_expectancy' as the y-axis encoding."
    return("Success")

def test_2_4c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert (answer.encoding.color.shorthand in {'region', 'region:nominal', 'region:N'} or 
            answer.encoding.color.field in {'region', 'region:nominal', 'region:N'}), "Make sure you are using 'region' as the color encoding."
    assert (answer.encoding.size.shorthand in {'population', 'population:quantitative', 'population:Q'} or 
            answer.encoding.size.field in {'population', 'population:quantitative', 'population:Q'}), "Make sure you are using 'population' as the color encoding."
    return("Success")

def test_2_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'z').encode('utf8')).hexdigest() != '763e59c2e07c2124503b3bef9e81977dfcbca6bd', "Your answer is incorrect. Please make sure your answer is in uppercase."
    assert sha1((answer + 'z').encode('utf8')).hexdigest() == '3f59e5bf0b4aa9d8ccce288b1ccc1597b1d66da3', "Your answer is incorrect. What appears to be the trend between the number of children per woman and life expectancy based on your plot in Question 2.4?"
    return("Success")

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 38982, "Your answer has incorrect number of rows. Please make sure you are returning the same number of rows as original dataframe."
    assert answer.shape[1] == 15, "Your answer has incorrect number of columns. Please make sure you are assining a new column named 'women_men_school_ratio'."
    assert 'women_men_school_ratio' in answer.columns, "Your answer is incorrect. Please make sure your new column has the correct name ('women_men_school_ratio')."
    assert answer.dtypes['women_men_school_ratio'] == 'float64', "Please make sure your new column is of float64 data type."
    return("Success")

def test_3_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 7832, "Your answer has incorrect number of rows. Please make sure you are filtering for only the observations between years 1971 and 2014, inclusive."
    assert answer.shape[1] == 15, "Your answer has incorrect number of columns. Please make sure you are returning the same number of columns as the gapminder_ratio_df dataframe"
    assert len(set(answer['year'])) == 44, "Your answer is incorrect. Please make sure the 'year' column is of type datetime and you are filtering for only the observations between years 1971 and 2014, inclusive."
    return("Success")

def test_3_3a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert answer.mark == 'line', "Make sure you are using the correct mark type."
    return("Success")

def test_3_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert (answer.encoding.x.shorthand in {'year', 'year:temporal', 'year:T'} or 
            answer.encoding.x.field in {'year', 'year:temporal', 'year:T'}), "Make sure you are using 'year' as the x-axis encoding."
    assert (answer.encoding.y.shorthand in {'mean(women_men_school_ratio)', 'mean(women_men_school_ratio):quantitative', 'mean(women_men_school_ratio):Q'} or 
            (answer.encoding.y.field in {'women_men_school_ratio', 'women_men_school_ratio:quantitative', 'women_men_school_ratio:Q'} and 
             answer.encoding.y.aggregate == 'mean')), "Make sure you are using mean of the 'women_men_school_ratio' as the y-axis encoding."
    return("Success")

def test_3_3c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert (answer.encoding.color.shorthand in {'income_group', 'income_group:nominal', 'income_group:N', 'income_group:ordinal', 'income_group:O'} or 
            answer.encoding.color.field in {'income_group', 'income_group:nominal', 'income_group:N', 'income_group:ordinal', 'income_group:O'}), "Make sure you are using 'income_group' as the color encoding."
    return("Success")

def test_3_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to bubble_plot."
    assert answer.mark == 'line', "Make sure you are using the correct mark type."
    assert (answer.encoding.x.shorthand in {'year', 'year:temporal', 'year:T'} or 
            answer.encoding.x.field in {'year', 'year:temporal', 'year:T'}), "Make sure you are using 'year' as the x-axis encoding."
    assert (answer.encoding.y.shorthand in {'mean(women_men_school_ratio)', 'mean(women_men_school_ratio):quantitative', 'mean(women_men_school_ratio):Q'} or 
            (answer.encoding.y.field in {'women_men_school_ratio', 'women_men_school_ratio:quantitative', 'women_men_school_ratio:Q'} and 
             answer.encoding.y.aggregate == 'mean')), "Make sure you are using mean of the 'women_men_school_ratio' as the y-axis encoding."
    assert (answer.encoding.color.shorthand in {'income_group', 'income_group:nominal', 'income_group:N', 'income_group:ordinal', 'income_group:O'} or 
            answer.encoding.color.field in {'income_group', 'income_group:nominal', 'income_group:N', 'income_group:ordinal', 'income_group:O'}), "Make sure you are using 'income_group' as the color encoding."
    assert answer.encoding.color.sort == ['High', 'Upper middle', 'Lower middle', 'Low'], "Make sure you are sorting the color encoding in the order 'High', 'Upper middle', 'Lower middle', 'Low'."
    return("Success")

def test_3_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == list, "Your answer is incorrect. Please make sure your answer is a list of upper case letter(s)."
    assert len(answer) == 3, "Your answer is incorrect. Hint: There are 3 correct answers."
    # sort the list and concatenate into a string before checking answer
    assert sha1("".join(sorted(map(str.upper, answer))).encode('utf8')).hexdigest() == '5c8072153f0ee1a27d9b8b1166fed8bb1c4b853f', "Your answer is incorrect. Can you review your plot from Question 3.5 to determine which 3 statements are correct?"
    return("Success")

def test_4_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to plot_dim."
    assert answer.width == 700, "Your plot width does not seem to be correct. Did you specify width argument as 700?"
    assert answer.height == 400, "Your plot height does not seem to be correct. Did you specify height argument as 400?"
    return("Success")

def test_4_3a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to title_plot."
    assert answer.encoding.y.title != alt.utils.schemapi.Undefined, "Your y-axis does not appear to have a title yet. Did you assign a proper title for the y-axis?"
    assert type(answer.encoding.y.title) == str, "Your y-axis title should be of type str. Did you assign a proper title for the y-axis?"
    assert not answer.encoding.y.title.islower(), "Your y-axis title does not contain any capitalization. Did you assign a proper title for the y-axis?"
    assert not '_' in answer.encoding.y.title, "Your y-axis title contains underscore(s). Did you assign a proper title for the y-axis?"
    assert "year" in answer.encoding.y.title.lower(), "Your y-axis label does not appear to have an appropriate unit. Did you specify the unit for life expectancy in y-axis label?"
    return("Success")

def test_4_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to title_plot."
    assert answer.encoding.color.title != alt.utils.schemapi.Undefined, "Your color legend does not appear to have a title yet. Did you assign a proper title for the color legend?"
    assert type(answer.encoding.color.title) == str, "Your color legend title should be of type str. Did you assign a proper title for the color legend?"
    assert not answer.encoding.color.title.islower(), "Your color legend title does not contain any capitalization. Did you assign a proper title for the color legend?"
    assert not '_' in answer.encoding.color.title, "Your color legend title contains underscore(s). Did you assign a proper title for the color legend?"
    return("Success")

def test_4_3c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == type(alt.Chart()), "Your answer is not an altair Chart object. Check to make sure that you have assigned an alt.Chart object to title_plot."
    assert answer.encoding.size.title != alt.utils.schemapi.Undefined, "Your size legend does not appear to have a title yet. Did you assign a proper title for the size legend?"
    assert type(answer.encoding.size.title) == str, "Your size legend title should be of type str. Did you assign a proper title for the size legend?"
    assert not answer.encoding.size.title.islower(), "Your size legend title does not contain any capitalization. Did you assign a proper title for the size legend?"
    assert not '_' in answer.encoding.size.title, "Your size legend title contains underscore(s). Did you assign a proper title for the size legend?"
    return("Success")
