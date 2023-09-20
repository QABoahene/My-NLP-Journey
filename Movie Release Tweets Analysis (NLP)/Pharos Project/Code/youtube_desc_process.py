from empath_data_processing import *

# A function to process youtube description from a database and create the empath theme column
def desc_to_emp(data, desc_col):
    data["Emptah Themes"] = data[desc_col].apply(strip).apply(topics_to_empath).apply(empath_to_tags).apply(lambda x: ' '.join(x))
    return data

#youtube_database
#empath_database = desc_to_emp(youtube_database, 'Description')