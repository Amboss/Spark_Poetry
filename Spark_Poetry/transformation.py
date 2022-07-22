import pyspark.sql.functions as F
import quinn


def with_greetings(df):
    """
    Test DataFrame
    :param df:
    :return:
    """
    return df.withColumn("Greetings", F.lit("hello!"))


def with_clean_first_name(df):
    """
    Test DF to practice Quinn functions
    :param df:
    :return:
    """
    return df.withColumn(
        "Clean_first_name",
        quinn.remove_non_word_characters(F.col("first_name"))
    )
