from hashlib import sha1
import pandas as pd
import pytest
import sys
import numpy as np
import altair as alt
from vega_datasets import data

# Disable maximum number of rows restriction
alt.data_transformers.disable_max_rows()

# Question 1
players_url = 'https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/data/baseball_players.json'
# Question 3.2
state_url = 'https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/data/states_df.json'
# Question 3.3
pitcher_url = 'https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/data/baseball_pitchers.json'
# Question 5
batting_url = 'https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/data/baseball_players_stats.json'


def test_1_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == pd.DataFrame, "Your answer should be a pandas DataFrame."
    assert answer.shape[0] == 19074, "Your dataframe has incorrect number of rows."
    assert answer.shape[1] == 23, "Your dataframe has incorrect number of columns." 
    assert (set(answer.columns) == 
            {'bats','birth_city','birth_country','birth_date','birth_day','birth_month','birth_state',
             'birth_year','death_country','death_state','death_year','debut','final_game','height','id',
             'id_country','name_first','name_given','name_last','playerID','region','throws','weight'}
           ), "Columns in this DataFrame do not match the columns in the original DataFrame."
    assert (answer["height"].sum() == 1380703 and
            answer["weight"].sum() == 3586630), "Values in this DataFrame do not match values in the original DataFrame"
    return("Success")


def test_1_3a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert (answer.mark != alt.utils.schemapi.Undefined and
            answer.mark.type == 'circle'), "Make sure you are using circle mark type."
    assert answer.mark.size == 20, "Make sure you are specifying mark size of 20"
    
    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        answer.encoding.x.shorthand in {'height:quantitative', 'height:Q'} or
        answer.encoding.x.type == 'quantitative' and (
            answer.encoding.x.shorthand == 'height' or answer.encoding.x.field == 'height'
        )           
    ), "Make sure you use 'height' as the X-axis encoding and specify that it is of 'quantitative' type."
    assert (answer.encoding.x.scale != alt.utils.schemapi.Undefined and
            answer.encoding.x.scale.zero == False), "Make sure you specify that 0 mark should not be included in X-axis."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        answer.encoding.y.shorthand in {'weight:quantitative', 'weight:Q'} or
        answer.encoding.y.type == 'quantitative' and (
            answer.encoding.y.shorthand == 'weight' or answer.encoding.y.field == 'weight'
        )
    ), "Make sure you use 'weight' as the Y-axis encoding and specify that it is of 'quantitative' type."
    assert (answer.encoding.y.scale != alt.utils.schemapi.Undefined and
            answer.encoding.y.scale.zero == False), "Make sure you specify that 0 mark should not be included in Y-axis."
    
    assert answer.encoding.color != alt.utils.schemapi.Undefined and (
        answer.encoding.color.shorthand in {'region:nominal', 'region:N'} or
        answer.encoding.color.type == 'nominal' and (
            answer.encoding.color.shorthand == 'region' or answer.encoding.color.field == 'region'
        )
    ), "Make sure you use 'region' as the Color encoding and specify that it is of 'nominal' type."
    return("Success")


def test_1_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        type(answer.encoding.x.title) == str and len(answer.encoding.x.title) > 5
    ), "Make sure you are providing a descriptive label for your X-axis."
    assert not answer.encoding.x.title.islower(), "Make sure your X-axis label is capitalized."
    assert 'in' in answer.encoding.x.title.lower(), "Make sure you include unit for the X-axis label."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        type(answer.encoding.y.title) == str and len(answer.encoding.y.title) > 5
    ), "Make sure you are providing a descriptive label for your Y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure your Y-axis label is capitalized."
    assert ('pound' in answer.encoding.y.title.lower() or 
            'lb' in answer.encoding.y.title.lower()), "Make sure you include unit for the Y-axis label."
    
    assert answer.encoding.color != alt.utils.schemapi.Undefined and (
        type(answer.encoding.color.title) == str and len(answer.encoding.color.title) > 5
    ), "Make sure you are providing a descriptive label for your Color encoding legend."
    assert not answer.encoding.color.title.islower(), "Make sure your Color encoding legend label is capitalized."

    assert type(answer.title) == str and len(answer.title) > 5, "Make sure you are providing a descriptive title for your plot."
    assert not answer.title.islower(), "Make sure your plot title is capitalized."    
    return("Success")


def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert (type(answer.encoding.tooltip) == list and
            len(answer.encoding.tooltip) == 3), "Your tooltip should have 3 channels ('name_first', 'name_last', and 'birth_country')."
    test_tooltips = ["name_first", "name_last", "birth_country"]
    included_tooltip = []
    for answer_tooltip in answer.encoding.tooltip:
        for test_tooltip in test_tooltips:
            if (answer_tooltip.shorthand in {f"{test_tooltip}:nominal", f"{test_tooltip}:N"} or
                answer_tooltip.type == 'nominal' and (
                    answer_tooltip.shorthand == test_tooltip or answer_tooltip.field == test_tooltip)):
                included_tooltip.append(test_tooltip)
    not_included = set(test_tooltips).difference(set(included_tooltip))
    assert len(not_included) == 0, f"Your tooltip does not include {list(not_included)[0]} channel. Make sure you also specify that it is of 'nominal' type."
    return("Success")


def test_1_5a(answer):
    assert not answer is None, "Your answer for select_region does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Selection, "Your answer for select_region should be an altair Selection object."
    assert answer.selection != alt.utils.schemapi.Undefined and (
        answer.selection.type == 'multi'
    ), "Make sure to define select_region using 'selection_multi()' function."
    assert answer.selection.fields == ['region'], "Make sure you specify that you want to select on the 'region' fields. Hint: 'fields' argument should be a list."
    assert answer.selection.bind == 'legend', "Make sure you specify that you want to bind the 'legend'."
    return("Success")


def test_1_5b(answer1, answer2):
    assert not answer1 is None, "Your answer for select_region does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for select_region should be an altair Selection object."
    assert not answer2 is None, "Your answer for hw_legend_plot does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for hw_legend_plot should be an altair Chart."
    assert answer2.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer1.name in answer2.selection and
        answer1.selection == answer2.selection[answer1.name]
    ), "Make sure you add select_region to hw_legend_plot using 'add_selection'."
    return("Success")


def test_1_5c(answer):
    assert not answer is None, "Your answer for hw_legend_plot does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer for hw_legend_plot should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert (answer.encoding.opacity != alt.utils.schemapi.Undefined and 
            answer.selection != alt.utils.schemapi.Undefined and
            answer.encoding.opacity.condition != alt.utils.schemapi.Undefined), "Make sure you set the opacity channel to a condition depending on select_region."
    assert answer.encoding.opacity.condition.selection in answer.selection and (
        (answer.encoding.opacity.value == 0 and answer.encoding.opacity.condition.value == 0.8) or
        (answer.encoding.opacity.value == 0.8 and answer.encoding.opacity.condition.value == 0)
    ), "Make sure you set opacity to 0 or 0.8 depending on select_region."
    assert (
        answer.encoding.opacity.value == 0 and 
        answer.encoding.opacity.condition.value == 0.8
    ), "You're very close. Make sure you set opacity to 0.8 when the corresponding region is selected, and 0 when the region is not selected."
    return("Success")


def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == int, "Make sure your answer is an object of type int."
    assert (
        sha1((str(answer)+'i').encode('utf8')).hexdigest() == '7eb05f281d790790f78faabeb621483c68bf74dd'
    ), "Your answer is incorrect. Try clicking 'Africa' region in the legend to see how many players are from Africa." 
    return("Success")


def test_2_1a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert (answer.mark != alt.utils.schemapi.Undefined and 
            (answer.mark == 'bar' or answer.mark.type == 'bar')), "Make sure you are using bar mark type."
    assert not 'color' in str(answer.encoding), "Please don't encode a variable to the color channel and instead set a static color in the mark method."
    assert 'color' in str(answer.mark), "Make sure you are giving your bar plot a nice colour other than the default colour."

    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        answer.encoding.x.shorthand in {'birth_year:temporal', 'birth_year:T'} or
        answer.encoding.x.type == 'temporal' and (
            answer.encoding.x.shorthand == 'birth_year' or answer.encoding.x.field == 'birth_year'
        )           
    ), "Make sure you use 'birth_year' as the X-axis encoding and specify that it is of 'temporal' type."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        answer.encoding.y.shorthand in {'count():quantitative', 'count():Q'} or (
            # Not a typo. Use 'count' instead of 'count()' when it is an aggregate instead of a field/shorthand
            answer.encoding.y.shorthand == 'count()' or answer.encoding.y.aggregate == 'count'
        )          
    ), "Make sure you use 'count()' as the Y-axis encoding. You may need to specify that it is of 'quantitative' type."
    return("Success")


def test_2_1b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        type(answer.encoding.x.title) == str and len(answer.encoding.x.title) > 5
    ), "Make sure you are providing a descriptive label for your X-axis."
    assert not answer.encoding.x.title.islower(), "Make sure your X-axis label is capitalized."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        type(answer.encoding.y.title) == str and len(answer.encoding.y.title) > 5
    ), "Make sure you are providing a descriptive label for your Y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure your Y-axis label is capitalized."
    
    # Not a typo. This plot should not have a title. 
    assert answer.title == alt.utils.schemapi.Undefined, "Make sure you don't give this plot any title."
    return("Success")


def test_2_2a(answer):
    assert not answer is None, "Your answer for interval does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Selection, "Your answer for interval should be an altair Selection object."
    assert answer.selection != alt.utils.schemapi.Undefined and (
        answer.selection.type == 'interval'
    ), "Make sure to define 'interval' using 'selection_interval()' function."
    assert "['x']" in str(answer.selection), "Make sure to specify that you want to select on the 'x'-axis encoding."
    assert answer.selection.encodings == ['x'], "Make sure you specify that you want to select on the 'x'-axis encoding. Hint: 'encodings' argument should be a list."
    return("Success")


def test_2_2b(answer1, answer2):
    assert not answer1 is None, "Your answer for interval does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for interval should be an altair Selection object."
    assert not answer2 is None, "Your answer for bar_slider does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for bar_slider should be an altair Chart."
    assert answer2.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer1.name in answer2.selection and 
        answer1.selection == answer2.selection[answer1.name]
    ), "Make sure you add interval to bar_slider using 'add_selection'."
    
    assert (answer2.encoding.color != alt.utils.schemapi.Undefined and 
            answer2.selection != alt.utils.schemapi.Undefined and
            answer2.encoding.color.condition != alt.utils.schemapi.Undefined), "Make sure you set the color channel for bar_slider to a condition depending on select_region."
    assert answer2.encoding.color.condition.selection in answer2.selection and (
        hasattr(answer2.encoding.color.condition, 'value') and
        type(answer2.encoding.color.value) == str and 
        type(answer2.encoding.color.condition.value) == str and 
        (answer2.encoding.color.value.lower() == 'lightgray' and answer2.encoding.color.condition.value.lower() == 'navy') or 
        (answer2.encoding.color.value.lower() == 'navy' and answer2.encoding.color.condition.value.lower() == 'lightgray')
    ), "Make sure you set color to 'lightgray' or 'navy' depending on select_region."
    assert (
        answer2.encoding.color.value.lower() == 'lightgray' and 
        answer2.encoding.color.condition.value.lower() == 'navy'
    ), "You're very close. Make sure you set color to 'navy' when the corresponding region is selected, and 'lightgray' when the region is not selected."    
    assert answer2.height == 100, "Make sure you set height for bar_slider to 100."
    assert answer2.width == 600, "Make sure you set width for bar_slider to 600."
    return("Success")


def test_2_2c(answer1, answer2):
    assert not answer1 is None, "Your answer for interval does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for interval should be an altair Selection object."
    assert not answer2 is None, "Your answer for scatter_plot does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for scatter_plot should be an altair Chart."
    assert answer2.data == players_url, "Make sure you are using players_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer1.name in answer2.selection and 
        answer1.selection == answer2.selection[answer1.name]
    ), "Make sure you add interval to scatter_plot using 'add_selection'."
    
    assert (answer2.encoding.color != alt.utils.schemapi.Undefined and 
            answer2.selection != alt.utils.schemapi.Undefined and
            answer2.encoding.color.condition != alt.utils.schemapi.Undefined), "Make sure you set the color channel for scatter_plot to a condition depending on select_region."
    assert answer2.encoding.color.condition.selection in answer2.selection and (
        (hasattr(answer2.encoding.color, 'value') and
         type(answer2.encoding.color.value) == str and 
         answer2.encoding.color.value.lower() == 'lightgray' and answer2.encoding.color.condition.shorthand in {'region:nominal', 'region:N'}) or 
        (hasattr(answer2.encoding.color.condition, 'value') and
         type(answer2.encoding.color.condition.value) == str and 
         answer2.encoding.color.shorthand in {'region:nominal', 'region:N'} and answer2.encoding.color.condition.value.lower() == 'lightgray')
    ), "Make sure you set color to 'region' with nominal datatype or 'lightgray' depending on select_region."
    assert (
        hasattr(answer2.encoding.color, 'value') and
        type(answer2.encoding.color.value) == str and
        answer2.encoding.color.value.lower() == 'lightgray' and 
        answer2.encoding.color.condition.shorthand in {'region:nominal', 'region:N'} 
    ), "You're very close. Make sure you set color to 'region' with nominal datatype when the corresponding region is selected, and 'lightgray' when the region is not selected."
    
    assert (
        (answer2.encoding.opacity.value == 0.01 and answer2.encoding.opacity.condition.value == 0.8) or 
        (answer2.encoding.opacity.value == 0.8 and answer2.encoding.opacity.condition.value == 0.01)
    ), "Make sure you set color to '0.01' or '0.8' depending on select_region."
    assert (
        answer2.encoding.opacity.value == 0.01 and 
        answer2.encoding.opacity.condition.value == 0.8 
    ), "You're very close. Make sure you set opacity to 0.8 when the corresponding region is selected, and 0 when the region is not selected."
    assert answer2.width == 600, "Make sure you set width for scatter_plot to 600."
    return("Success")


def test_2_2d(answer1, answer2, answer3):
    assert not answer1 is None, "Your answer for bar_slider does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer for scatter_plot does not exist. Have you passed in the correct variable?"
    assert not answer3 is None, "Your answer for dob_combo_plot does not exist. Have you passed in the correct variable?"
    
    assert type(answer1) == alt.Chart, "Your answer for bar_slider should be an altair Chart."
    assert type(answer2) == alt.Chart, "Your answer for scatter_plot should be an altair Chart."
    assert type(answer3) == alt.VConcatChart, "Your answer for dob_combo_plot should be an altair VConcatChart."
    
    assert len(answer3.vconcat) == 2, "Make sure dob_combo_plot has 2 rows."
    plot3 = answer3.copy()
    plot1 = plot3.vconcat.pop(0); plot1.data = answer3.data
    plot2 = plot3.vconcat.pop(0); plot2.data = answer3.data
    
    # Test fails when color is not all lowercase. Display warning message to suggest using lowercase.
    assert (
        answer1.encoding.color.value.islower() and 
        answer1.encoding.color.condition.value.islower() and
        (not hasattr(answer2.encoding.color, 'value') or answer2.encoding.color.value.islower()) and
        (not hasattr(answer2.encoding.color.condition, 'value') or answer2.encoding.color.condition.value.islower())
    ), "Please make sure that color values are all in lowercase: e.g. 'lightgray' instead of 'Lightgray'."
    
    assert (
        (plot1.to_dict() == answer1.to_dict() and plot2.to_dict() == answer2.to_dict()) or
        (plot1.to_dict() == answer2.to_dict() and plot2.to_dict() == answer1.to_dict())
    ), "Make sure you create dob_combo_plot by vertically stacking bar_slider and scatter_plot."
    return("Success")


def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.UrlData, "Your answer should be an altair UrlData."
    assert answer.url == data.us_10m.url, "Make sure you are using the correct url for the data (us_10m from the vega_datasets)."
    assert answer.format != alt.utils.schemapi.Undefined and (
        answer.format.feature == 'states' and
        answer.format.type == 'topojson'
    ), "Make sure you are using topo_feature() to load 'states' feature from us_10m data."
    return("Success")


def test_3_2a(answer):
    assert not answer is None, "Your answer for background does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer for background should be an altair Chart."
    assert type(answer.data) == alt.UrlData and (
        answer.data.url == data.us_10m.url
    ), "Make sure you are using the correct url for the data (us_10m from the vega_datasets)."
    
    assert (answer.mark != alt.utils.schemapi.Undefined and 
            answer.mark.type == 'geoshape'), "Make sure you are using .mark_geoshape() for background."
    assert answer.mark.color == 'white', "Make sure you are giving white color to geoshape mark for background."
    assert answer.mark.stroke == 'grey', "Make sure you are giving grey stroke to geoshape mark for background."
    return("Success")


def test_3_2b(answer, answer2):
    assert not answer is None, "Your answer for states_plot does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer for states_plot should be an altair Chart."
    assert type(answer.data) == alt.UrlData and ( 
        answer.data.url == data.us_10m.url
    ), "Make sure you are using the correct url for the data (us_10m from the vega_datasets)."
    
    assert (answer.mark != alt.utils.schemapi.Undefined and 
            answer.mark.type == 'geoshape'), "Make sure you are using .mark_geoshape() for states_plot."
    assert answer.mark.stroke == 'black', "Make sure you are giving black stroke to geoshape mark for states_plot."
    assert answer.mark.strokeWidth == 0.15, "Make sure you are giving strokeWidth of 0.15 to geoshape mark for states_plot."
    
    assert (
        answer.encoding.color != alt.utils.schemapi.Undefined and 
        answer.encoding.color.scale != alt.utils.schemapi.Undefined and
        answer.encoding.color.scale.scheme != alt.utils.schemapi.Undefined
    ), "Make sure you specify an appropriate colour scheme setting within the Color channel. Hint: use scale=alt.Scale(scheme=...)."
    assert (
        type(answer.encoding.color.title) == str and len(answer.encoding.color.title) > 5
    ), "Make sure you are providing a descriptive label for your Color channel."
    assert not answer.encoding.color.title.islower(), "Make sure your Color channel label is capitalized."
    assert 'Undefined' in str(answer2.layer[0].encoding), "make sure that your `players_map` plot is made by adding `background` plot first followed by `states_plot`."
    return("Success")


def test_3_2c(answer):
    assert not answer is None, "Your answer for states_plot does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer for states_plot should be an altair Chart."
    assert (type(answer.encoding.tooltip) == list and
            len(answer.encoding.tooltip) == 2), "Your tooltip should have 2 channels ('birth_state:N' and 'player_num:Q')."
    
    assert (
        alt.Tooltip("birth_state:N", title="State") in answer.encoding.tooltip
    ), 'Make sure tooltip for states_plot includes alt.Tooltip("birth_state:N", title="State").'
    assert (
        alt.Tooltip("player_num:Q", title="Number of players") in answer.encoding.tooltip
    ), 'Make sure tooltip for states_plot includes alt.Tooltip("player_num:Q", title="Number of players").'
    return("Success")


def test_3_2d(answer):
    assert not answer is None, "Your answer for states_plot does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer for states_plot should be an altair Chart."
    assert type(answer.transform) == list, "Make sure you use .transform_lookup() to look up data from state_url." 
    assert len(answer.transform) == 1, "Make sure you don't have any data transformation aside from .transform_lookup()."
    assert type(answer.transform[0]) == alt.LookupTransform, "Make sure you use .transform_lookup() to look up data from state_url."
    assert answer.transform[0].lookup == 'id', "Make sure you set the lookup argument to 'id'."
    assert 'from' in answer.transform[0].to_dict() and (
        type(answer.transform[0]['from'])== alt.LookupData
    ), "Make sure you use alt.LookupData() for from_ argument in alt.transform_lookup() to specify looking up data from state_url."
    assert answer.transform[0]['from'].data == state_url, "Make sure you are specifying the correct url to look up data from. Hint: use data argument in alt.LookupData()."
    assert answer.transform[0]['from'].key == 'id', "Make sure you specify that you are looking up by the 'id' column. Hint: use key argument in alt.LookupData()."
    assert type(answer.transform[0]['from'].fields) == list and (
        len(answer.transform[0]['from'].fields) == 2 and
        set(answer.transform[0]['from'].fields) == {"birth_state", "player_num"}
    ), "Make sure you select the columns 'birth_state' and 'player_num' from data source. Hint: use fields argument in alt.LookupData()."
    return("Success")


def test_3_2e(answer1, answer2, answer3):
    assert not answer1 is None, "Your answer for background does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Chart, "Your answer for background should be an altair Chart."
    assert not answer2 is None, "Your answer for states_plot does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for states_plot should be an altair Chart."
    assert not answer3 is None, "Your answer for players_map does not exist. Have you passed in the correct variable?"
    assert type(answer3) == alt.LayerChart, "Your answer for players_map should be an altair LayerChart."

    assert type(answer3.layer) == list, "Your answer for players_map should be an altair LayerChart with 2 layers."
    assert len(answer3.layer) == 2, "Make sure your players_map LayerChart has 2 layers."
    plot3 = answer3.copy()
    plot1 = plot3.layer.pop(0); plot1.data = answer3.data
    plot2 = plot3.layer.pop(0); plot2.data = answer3.data
    
    assert (
        (plot1.to_dict() == answer1.to_dict() and plot2.to_dict() == answer2.to_dict()) or
        (plot1.to_dict() == answer2.to_dict() and plot2.to_dict() == answer1.to_dict())
    ), "Make sure you create players_map by layering background and states_plot."
    
    assert answer3.height == 250, "Make sure you set the height for players_map LayerChart to 250."
    assert answer3.width == 500, "Make sure you set the width for players_map LayerChart to 500."
    assert answer3.projection != alt.utils.schemapi.Undefined and (
        answer3.projection.type == 'albersUsa'
    ), "Make sure you specify 'albersUsa' projection for players_map LayerChart."
    return("Success")


def test_3_3a(answer1, answer2):
    assert not answer1 is None, "Your answer for state_select does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for state_select should be an altair Selection object."
    assert not answer2 is None, "Your answer for states_select_map does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.LayerChart, "Your answer for states_select_map should be an altair LayerChart."

    assert answer1.selection != alt.utils.schemapi.Undefined and (
        answer1.selection.type == 'multi'
    ), "Make sure to define state_select using 'selection_multi()' function."
    assert answer1.selection.fields == ['id'], "Make sure you specify that you want to select on the 'id' fields. Hint: 'fields' argument should be a list."

    assert (answer2.encoding.opacity != alt.utils.schemapi.Undefined and 
            answer2.encoding.opacity.condition != alt.utils.schemapi.Undefined and
            answer2.encoding.opacity.condition.selection != alt.utils.schemapi.Undefined
           ), "Make sure you set the opacity channel to a condition depending on state_select."
    assert answer1.name == answer2.encoding.opacity.condition.selection and (
        (answer2.encoding.opacity.value == 0.2 and answer2.encoding.opacity.condition.value == 0.8) or
        (answer2.encoding.opacity.value == 0.8 and answer2.encoding.opacity.condition.value == 0.2)
    ), "Make sure you set opacity to 0.2 or 0.8 depending on state_select."
    assert (
        answer2.encoding.opacity.value == 0.2 and 
        answer2.encoding.opacity.condition.value == 0.8
    ), "You're very close. Make sure you set opacity to 0.8 when the corresponding birth_state is selected, and 0.2 when the birth_state is not selected."
    
    assert (type(answer2.encoding.tooltip) == list and
            len(answer2.encoding.tooltip) == 2), "Your tooltip should have 2 channels ('birth_state' and `player_num`)."
    assert (
        (answer2.encoding.tooltip[0].shorthand in {'birth_state:nominal', 'birth_state:N'}) or 
        (answer2.encoding.tooltip[0].type == 'nominal' and (
            answer2.encoding.tooltip[0].shorthand == 'birth_state' or answer2.encoding.tooltip[0].field == 'birth_state')
        )
    ), 'Make sure tooltip for states_select_map includes alt.Tooltip("birth_state:N", title="State").'
    assert (
        type(answer2.encoding.tooltip[0].title) == str and
        len(answer2.encoding.tooltip[0].title) > 5 and
        not answer2.encoding.tooltip[0].title.islower()
    ), 'Make sure to include descriptive label for tooltip with appropriate capitalization.'
    
    assert type(answer2.transform) == list, "Make sure you use .transform_lookup() to look up data from state_url." 
    assert len(answer2.transform) == 1, "Make sure you don't have any data transformation aside from .transform_lookup()."
    assert type(answer2.transform[0]) == alt.LookupTransform, "Make sure you use .transform_lookup() to look up data from state_url."
    assert answer2.transform[0].lookup == 'id', "Make sure you set the lookup argument to 'id'."
    assert 'from' in answer2.transform[0].to_dict() and (
        type(answer2.transform[0]['from'])== alt.LookupData
    ), "Make sure you use alt.LookupData() for from_ argument in alt.transform_lookup() to specify looking up data from state_url."
    assert answer2.transform[0]['from'].data == state_url, "Make sure you are specifying the correct url to look up data from. Hint: use data argument in alt.LookupData()."
    assert answer2.transform[0]['from'].key == 'id', "Make sure you specify that you are looking up by the 'id' column. Hint: use key argument in alt.LookupData()."
    assert type(answer2.transform[0]['from'].fields) == list and (
        len(answer2.transform[0]['from'].fields) == 2 and
        set(answer2.transform[0]['from'].fields) == {"birth_state", "player_num"}
    ), "Make sure you select the columns 'birth_state' and 'player_num' from data source. Hint: use fields argument in alt.LookupData()."
    return("Success")


def test_3_3b(answer1, answer2):
    assert not answer1 is None, "Your answer for state_select does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for state_select should be an altair Selection object."
    assert not answer2 is None, "Your answer for pitching_scatter does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for pitching_scatter should be an altair Chart."
    assert answer2.data == pitcher_url, "Make sure you are using pichers_url as a data source. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert (answer2.mark != alt.utils.schemapi.Undefined and
            answer2.mark.type == 'circle'), "Make sure you are using circle mark type."
    assert answer2.mark.size == 20, "Make sure you are specifying mark size of 20"
    
    assert answer2.encoding.x != alt.utils.schemapi.Undefined and (
        answer2.encoding.x.shorthand in {'ERA:quantitative', 'ERA:Q'} or
        answer2.encoding.x.type == 'quantitative' and (
            answer2.encoding.x.shorthand == 'ERA' or answer2.encoding.x.field == 'ERA'
        )           
    ), "Make sure you use 'ERA' as the X-axis encoding and specify that it is of 'quantitative' type."
    assert (answer2.encoding.x.scale != alt.utils.schemapi.Undefined and
            answer2.encoding.x.scale.domain == [0, 55]), "Make sure you specify scale with domain [0, 55] for X-axis."
    assert type(answer2.encoding.x.title) == str and len(answer2.encoding.x.title) > 5, "Make sure you are providing a descriptive label for your X-axis."
    assert not answer2.encoding.x.title.islower(), "Make sure your X-axis label is capitalized."
    
    assert answer2.encoding.y != alt.utils.schemapi.Undefined and (
        answer2.encoding.y.shorthand in {'SO_per_BF:quantitative', 'SO_per_BF:Q'} or
        answer2.encoding.y.type == 'quantitative' and (
            answer2.encoding.y.shorthand == 'SO_per_BF' or answer2.encoding.y.field == 'SO_per_BF'
        )
    ), "Make sure you use 'SO_per_BF' as the Y-axis encoding and specify that it is of 'quantitative' type."
    assert (answer2.encoding.y.scale != alt.utils.schemapi.Undefined and
            answer2.encoding.y.scale.domain == [0, 0.5]), "Make sure you specify scale with domain [0, 0.5] for Y-axis."
    assert type(answer2.encoding.y.title) == str and len(answer2.encoding.x.title) > 5, "Make sure you are providing a descriptive label for your Y-axis."
    assert not answer2.encoding.y.title.islower(), "Make sure your Y-axis label is capitalized."
    
    assert (type(answer2.encoding.tooltip) == list and
            len(answer2.encoding.tooltip) == 2), 'Your tooltip should have 2 channels ("name_first:N", "name_last:N").'
    test_tooltips = ["name_first", "name_last"]
    included_tooltip = []
    for answer_tooltip in answer2.encoding.tooltip:
        for test_tooltip in test_tooltips:
            if (answer_tooltip.shorthand in {f"{test_tooltip}:nominal", f"{test_tooltip}:N"} or
                answer_tooltip.type == 'nominal' and (
                    answer_tooltip.shorthand == test_tooltip or answer_tooltip.field == test_tooltip)):
                included_tooltip.append(test_tooltip)
    not_included = set(test_tooltips).difference(set(included_tooltip))
    assert len(not_included) == 0, f"Your tooltip does not include {list(not_included)[0]} channel. Make sure you also specify that it is of 'nominal' type."
    
    assert answer2.width == 500, "Make sure you set width for pitching_scatter to 500."
    assert type(answer2.title) == str and len(answer2.title) > 5, "Make sure you are providing a descriptive title for pitching_scatter plot."
    assert not answer2.title.islower(), "Make sure your plot title for pitching_scatter is capitalized."
    return("Success")


def test_3_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'t').encode('utf8')).hexdigest() == '589e942e00a7dd64a273deb5041c7ce469f2bad7'
    ), "Double-check your answer by selecting the pitcher with the highest strikeout rate and lowest ERA and checking the map for the corresponding birth_state."
    return("Success")


def test_4_1b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == players_url, "Make sure you are using players_url as a data source. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        type(answer.encoding.x.title) == str and len(answer.encoding.x.title) > 5
    ), "Make sure you are providing a descriptive label for your X-axis."
    assert not answer.encoding.x.title.islower(), "Make sure your X-axis label is capitalized."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        type(answer.encoding.y.title) == str and len(answer.encoding.y.title) > 5
    ), "Make sure you are providing a descriptive label for your Y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure your Y-axis label is capitalized."
    
    assert type(answer.encoding.y.sort) == list and ( 
        answer.encoding.y.sort==["L", "R", "B", "No record"]
    ), 'Make sure you specify Y-axis to be sorted in the following order: ["L", "R", "B", "No record"]'
    
    assert answer.encoding.y.scale != alt.utils.schemapi.Undefined and (
        answer.encoding.y.scale.domain == ["L", "R", "B", "No record"]
    ), 'Make sure you specify Y-axis to have the following domain: ["L", "R", "B", "No record"]'
    
    # Not a typo. This plot should not have a title. 
    assert answer.title == alt.utils.schemapi.Undefined, "Make sure you don't give this plot any title."
    return("Success")


def test_4_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'e').encode('utf8')).hexdigest() == 'b452d6b23b3c28f85872fffd99bdaf90ce0ad44a'
    ), "Double-check what proportion of batters use left/right/both hand(s)."
    return("Success")


def test_4_3a(answer1, answer2):
    assert not answer1 is None, "Your answer for state_select does not exist. Have you passed in the correct variable?" 
    assert type(answer1) == alt.Selection, "Your answer for state_select should be an altair Selection object."
    assert not answer2 is None, "Your answer for filtered_bats_bars does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for filtered_bats_bars should be an altair Chart."
    assert answer2.data == players_url, "Make sure you are using players_url as a data source. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert type(answer2.transform) == list and (
        len(answer2.transform) == 1
    ), "Make sure you don't have any data transformation aside from .transform_filter()."
    assert type(answer2.transform[0]) == alt.FilterTransform, "Make sure you use .transform_filter() to add a transformation filter to the bats_plot."
    assert answer1.name in answer2.transform[0].filter.values(), "Make sure you use .transform_filter() to add the state_select selection tool as a transformation filter to the bats_plot."
    return("Success")


def test_4_3b(answer1, answer2, answer3):
    assert not answer1 is None, "Your answer for states_select_map does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer for filtered_bats_bars does not exist. Have you passed in the correct variable?"
    assert not answer3 is None, "Your answer for map_bat_plot does not exist. Have you passed in the correct variable?"

    assert type(answer1) == alt.LayerChart, "Your answer for states_select_map should be an altair LayerChart."
    assert type(answer2) == alt.Chart, "Your answer for filtered_bats_bars should be an altair Chart."
    assert type(answer3) == alt.VConcatChart, "Your answer for map_bat_plot should be an altair VConcatChart. That means the plots should be on top of each other."

    assert type(answer3.vconcat) == list and (
        len(answer3.vconcat) == 2
    ), "Make sure map_bat_plot has 2 rows."

    plot3 = answer3.copy()
    # The two subplots have separate data from VConcatChart
    plot1 = plot3.vconcat.pop(0)
    plot2 = plot3.vconcat.pop(0)

    assert (
        (plot1.to_dict() == answer1.to_dict() and plot2.to_dict() == answer2.to_dict()) or
        (plot1.to_dict() == answer2.to_dict() and plot2.to_dict() == answer1.to_dict())
    ), "Make sure you create map_bat_plot by vertically stacking states_select_map and filtered_bats_bars."
    return("Success")


def test_4_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'r').encode('utf8')).hexdigest() == '05c77e49f6a349a5f2d72739ecf59dfac5cffe9f'
    ), "Use state_select to filter players from Wyoming (WY), and check which side is the most dominant among these players."
    return("Success")


def test_4_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'a').encode('utf8')).hexdigest() == '6c0596b8ac609191181a90517d51c0b486f23799'
    ), "Use state_select to filter players from New York (NY), and check which side is the most dominant among these players."
    return("Success")


def test_4_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == int, "Make sure your answer is of type int."
    assert (
        sha1((str(answer)+'c').encode('utf8')).hexdigest() == 'ef5e0d9d29c7ac72796905afbc99fd404f2c7aac'
    ), "Use state_select to filter players from New Hampshire (NH), and check how many of these players bat using left hand."
    return("Success")


def test_5_2a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == batting_url, "Make sure you are using batting_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."

    assert answer.mark != alt.utils.schemapi.Undefined and (
        answer.mark == 'circle' or
        answer.mark.type == 'circle'
    ), "Make sure you are using circle mark type."
    
    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        answer.encoding.x.shorthand in {'HR:quantitative', 'HR:Q'} or (
            answer.encoding.x.type == 'quantitative' and (
                answer.encoding.x.shorthand == 'HR' or answer.encoding.x.field == 'HR'
            )
        )           
    ), "Make sure you use 'HR' as the X-axis encoding and specify that it is of 'quantitative' type."
    assert (answer.encoding.x.scale != alt.utils.schemapi.Undefined and
            answer.encoding.x.scale.domain == [0, 50]), "Make sure you specify scale with domain [0, 50] for X-axis."

    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        answer.encoding.y.shorthand in {'salary:quantitative', 'salary:Q'} or
        answer.encoding.y.type == 'quantitative' and (
            answer.encoding.y.shorthand == 'salary' or answer.encoding.y.field == 'salary'
        )
    ), "Make sure you use 'salary' as the Y-axis encoding and specify that it is of 'quantitative' type."
    assert (answer.encoding.y.scale != alt.utils.schemapi.Undefined and
            answer.encoding.y.scale.type == 'log' and
            answer.encoding.y.scale.domain == [500000, 50000000]), "Make sure you specify 'log' scale with domain [500000, 50000000] for Y-axis."
    
    assert answer.encoding.color != alt.utils.schemapi.Undefined and (
        answer.encoding.color.shorthand in {'team_name:nominal', 'team_name:N'} or
        answer.encoding.color.type == 'nominal' and (
            answer.encoding.color.shorthand == 'team_name' or answer.encoding.color.field == 'team_name'
        )
    ), "Make sure you use 'team_name' as the Color encoding and specify that it is of 'nominal' type."
    return("Success")


def test_5_2b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == alt.Chart, "Your answer should be an altair Chart."
    assert answer.data == batting_url, "Make sure you are using batting_url as a data source instead of the DataFrame object. Remember, this means you need to make sure to specify column datatypes to Altair."
    
    assert answer.encoding.x != alt.utils.schemapi.Undefined and (
        type(answer.encoding.x.title) == str and len(answer.encoding.x.title) > 5
    ), "Make sure you are providing a descriptive label for your X-axis."
    assert not answer.encoding.x.title.islower(), "Make sure your X-axis label is capitalized."
    
    assert answer.encoding.y != alt.utils.schemapi.Undefined and (
        type(answer.encoding.y.title) == str and len(answer.encoding.y.title) > 5
    ), "Make sure you are providing a descriptive label for your Y-axis."
    assert not answer.encoding.y.title.islower(), "Make sure your Y-axis label is capitalized."
    assert ('usd' in answer.encoding.y.title.lower() or 
            'dollar' in answer.encoding.y.title.lower() or
            '$' in answer.encoding.y.title.lower()), "Make sure you include unit for the Y-axis label."
    
    assert answer.encoding.color != alt.utils.schemapi.Undefined and (
        type(answer.encoding.color.title) == str and len(answer.encoding.color.title) > 3
    ), "Make sure you are providing a descriptive label for your Color encoding legend."
    assert not answer.encoding.color.title.islower(), "Make sure your Color encoding legend label is capitalized."

    assert (type(answer.encoding.tooltip) == list and
            len(answer.encoding.tooltip) == 3), "Your tooltip should have 3 channels ('name_first', 'name_last', and 'salary')."

    # 'salary' tooltip checked separately since specifying it as 'nominal', 'quantitative', or 'ordinal' datatypes 
    # doesn't matter for the purpose of this question (although it makes sense to specify it as 'quantitative').
    test_tooltips = ["name_first", "name_last"]
    tooltips_include_salary = False
    included_tooltip = []
    for answer_tooltip in answer.encoding.tooltip:
        # First check if answer_tooltip is a 'salary' tooltip
        if ((type(answer_tooltip.shorthand) == str and 'salary' in answer_tooltip.shorthand) or
            (type(answer_tooltip.field) == str and 'salary' in answer_tooltip.field)):
            tooltips_include_salary = True
            continue

        for test_tooltip in test_tooltips:
            if (answer_tooltip.shorthand in {f"{test_tooltip}:nominal", f"{test_tooltip}:N"} or
                answer_tooltip.type == 'nominal' and (
                    answer_tooltip.shorthand == test_tooltip or answer_tooltip.field == test_tooltip)):
                included_tooltip.append(test_tooltip)

    not_included = set(test_tooltips).difference(set(included_tooltip))
    assert len(not_included) == 0, f"Your tooltip does not include {list(not_included)[0]} channel. Make sure you also specify that it is of 'nominal' type."
    assert tooltips_include_salary, f"Your tooltip does not include 'salary' channel. Make sure you also specify the appropriate datatype."
    
    assert type(answer.title) == str and len(answer.title) > 5, "Make sure you are providing a descriptive title for your plot."
    assert not answer.title.islower(), "Make sure your plot title is capitalized."     
    
    return("Success")


def test_5_3a(answer):
    assert not answer is None, "Your answer for teams does not exist. Have you passed in the correct variable?"
    assert type(answer) == list, "Your answer for teams should be a list."
    assert len(answer) == 30, "Your answer for teams should be a list with 30 elements. Hint: make sure you are listing all the unique values in the team_name column. Are you using .unique() function?"
    correct_teams = ['Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 
                     'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 
                     'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 
                     'Los Angeles Angels of Anaheim', 'Los Angeles Dodgers', 'Miami Marlins', 
                     'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 
                     'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 
                     'San Francisco Giants', 'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 
                     'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']
    assert set(answer) == set(correct_teams), "Your answer for teams does not appear to have the correct values. Make sure you are listing all the unique values in the team_name column."
    assert answer == correct_teams, "You're very close. Make sure your answer for teams is sorted in the alphabetical order."
    return("Success")


def test_5_3b(answer1, answer2):
    assert not answer1 is None, "Your answer for teams does not exist. Have you passed in the correct variable?"
    assert type(answer1) == list, "Your answer for teams should be a list."
    assert not answer2 is None, "Your answer for dropdown_team does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.BindRadioSelect and (
        answer2.input == 'select'
    ), "Make sure you are using altair binding_select() for dropdown_team."

    assert sorted(answer2.options) == sorted(answer1), "Make sure dropdown_team uses teams as dropdown menu options."
    assert type(answer2.name) == str and len(answer2.name) > 3, "Make sure you are providing a descriptive name for your dropdown_team object."
    return("Success")


def test_5_3c(answer1, answer2):
    assert not answer1 is None, "Your answer for dropdown_team does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.BindRadioSelect, "Make sure you are using altair binding_select() when defining dropdown_team."   
    assert not answer2 is None, "Your answer for select_team does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Selection, "Your answer for select_team should be an altair Selection object."

    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer2.selection.type == 'single'
    ), "Make sure to define select_team using 'selection_single()' function."
    assert answer2.selection.bind == answer1, "Make sure you bind dropdown_team to select_team."
    assert answer2.selection.fields == ['team_name'], "Make sure you specify that you want to select on the 'team_name' fields. Hint: 'fields' argument should be a list."
    return("Success")


def test_5_3d(answer1, answer2):
    assert not answer1 is None, "Your answer for select_team does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for select_team should be an altair Selection object."
    assert not answer2 is None, "Your answer for stats_drop_plot does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for stats_drop_plot should be an altair Chart."
    
    assert answer2.encoding.color != alt.utils.schemapi.Undefined and (
        type(answer2.encoding.color.value) == str and
        answer2.encoding.color.value.lower() == 'navy'
    ), "Make sure to encode the colour channel for stats_drop_plot to a single colour 'navy'."
    
    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer1.name in answer2.selection and 
        answer1.selection == answer2.selection[answer1.name]
    ), "Make sure you add select_team to stats_drop_plot using 'add_selection'."

    assert type(answer2.transform) == list and (
        len(answer2.transform) == 1
    ), "Make sure you don't have any data transformation aside from .transform_filter()."
    assert type(answer2.transform[0]) == alt.FilterTransform, "Make sure you use .transform_filter() to add a transformation filter to the stats_drop_plot."
    assert answer1.name in answer2.transform[0].filter.values(), "Make sure you use .transform_filter() to add the select_team selection tool as a transformation filter to the stats_drop_plot."
    
    assert (answer2.encoding.opacity != alt.utils.schemapi.Undefined and 
            answer2.encoding.opacity.condition != alt.utils.schemapi.Undefined), "Make sure you set the opacity channel for stats_drop_plot to a condition depending on select_team."
    assert answer2.encoding.opacity.condition.selection in answer2.selection and (
        (answer2.encoding.opacity.value == 0.08 and answer2.encoding.opacity.condition.value == 0.8) or 
        (answer2.encoding.opacity.value == 0.8 and answer2.encoding.opacity.condition.value == 0.08)
    ), "Make sure you set opacity to 0.8 or 0.08 depending on select_team."
    assert (
        answer2.encoding.opacity.value == 0.08 and 
        answer2.encoding.opacity.condition.value == 0.8
    ), "You're very close. Make sure you set opacity to 0.8 when the corresponding region is selected, and 0.08 when the region is not selected."
    return("Success")


def test_5_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'t').encode('utf8')).hexdigest() == 'edfb92a5be2a31a47d117f6c1530e1cebe1b4963'
    ), "Use select_team to select each of the 4 teams listed, and check how much their high scoring home run players get paid."
    return("Success")


def test_5_5a(answer):
    assert not answer is None, "Your answer for batting_side does not exist. Have you passed in the correct variable?"
    assert type(answer) == list or type(answer) == np.ndarray, "Your answer for batting_side should be a list or a numpy.ndarray."
    assert len(answer) == 3, "Your answer for batting_side should be a list with 3 elements. Hint: make sure you are listing all the unique values in the bats column. Are you using .unique() function?"
    assert set(answer) == {'L', 'R', 'B'}, "Your answer for batting_side does not appear to have the correct values. Make sure you are listing all the unique values in the bats column."
    return("Success")


def test_5_5b(answer1, answer2):
    assert not answer1 is None, "Your answer for batting_side does not exist. Have you passed in the correct variable?"
    assert type(answer1) == list or type(answer1) == np.ndarray, "Your answer for batting_side should be a list or a numpy.ndarray."
    assert not answer2 is None, "Your answer for radio_batting does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.BindRadioSelect and (
        answer2.input == 'radio'
    ), "Make sure you are using altair binding_radio() for radio_batting."
    
    assert sorted(answer2.options) == sorted(answer1), "Make sure radio_batting uses batting_side as alt.binding_radio() options."
    assert type(answer2.name) == str and len(answer2.name) > 5, "Make sure you are providing a descriptive name for your radio_batting object."
    return("Success")


def test_5_5c(answer1, answer2, answer3):
    assert not answer1 is None, "Your answer for dropdown_team does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.BindRadioSelect, "Make sure you are using altair binding_select() when defining dropdown_team."    
    assert not answer2 is None, "Your answer for radio_batting does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.BindRadioSelect, "Make sure you are using altair binding_radio() when defining radio_batting."    
    assert not answer3 is None, "Your answer for select_bat_and_team does not exist. Have you passed in the correct variable?"
    assert type(answer3) == alt.Selection, "Your answer for select_bat_and_team should be an altair Selection object."

    assert answer3.selection != alt.utils.schemapi.Undefined and (
        answer3.selection.type == 'single'
    ), "Make sure to define select_bat_and_team using 'selection_single()' function."
    assert type(answer3.selection.bind) == dict, "Make sure to set the bind argument for alt.selection_single() to a dictionary."
    assert 'team_name' in answer3.selection.bind and (
        answer3['team_name'] == answer1
    ), "Make sure you bind dropdown_team to select_bat_and_team with 'team_name' as key."
    
    assert 'bats' in answer3.selection.bind and (
        answer3['bats'] == answer1
    ), "Make sure you bind radio_batting to select_bat_and_team with 'bats' as key."

    assert type(answer3.selection.fields) == list and (
        set(answer3.selection.fields) == {"bats", "team_name"}
    ), "Make sure you specify that you want to select on the 'bats' and 'team_name' fields. Hint: 'fields' argument should be a list."
    return("Success")


def test_5_5d(answer1, answer2):
    assert not answer1 is None, "Your answer for select_bat_and_team does not exist. Have you passed in the correct variable?"
    assert type(answer1) == alt.Selection, "Your answer for select_bat_and_team should be an altair Selection object."
    assert not answer2 is None, "Your answer for stats_radio_plot does not exist. Have you passed in the correct variable?"
    assert type(answer2) == alt.Chart, "Your answer for stats_radio_plot should be an altair Chart."
    
    assert answer2.encoding.color != alt.utils.schemapi.Undefined and (
        type(answer2.encoding.color.value) == str and
        answer2.encoding.color.value.lower() == 'navy'
    ), "Make sure to encode the colour channel for stats_radio_plot to a single colour 'navy'."
    
    assert answer2.selection != alt.utils.schemapi.Undefined and (
        answer1.name in answer2.selection and 
        answer1.selection == answer2.selection[answer1.name]
    ), "Make sure you add select_bat_and_team to stats_radio_plot using 'add_selection'."

    assert type(answer2.transform) == list and (
        len(answer2.transform) == 1
    ), "Make sure you don't have any data transformation aside from .transform_filter()."
    assert type(answer2.transform[0]) == alt.FilterTransform, "Make sure you use .transform_filter() to add a transformation filter to the stats_radio_plot."
    assert answer1.name in answer2.transform[0].filter.values(), "Make sure you use .transform_filter() to add the select_bat_and_team selection tool as a transformation filter to the stats_radio_plot."
    return("Success")


def test_5_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(answer) == str, "Make sure your answer is of type str."
    assert (
        sha1((answer.lower()+'i').encode('utf8')).hexdigest() == 'aab9b7bd17003da21256cca5c7d2d7ff4ea384b6'
    ), "Use select_bat_and_team to select San Diego Padres and each of 'L', 'R', and 'B' to check whether left-handed, right-handed, or ambidextrous players scored more home runs."
    return("Success")


