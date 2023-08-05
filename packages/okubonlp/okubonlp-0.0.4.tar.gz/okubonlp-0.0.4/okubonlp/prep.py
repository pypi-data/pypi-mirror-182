import pandas as pd
import string
import re


def split_datecolumn(df, date_column):
    """日付を分割させカテゴリ値として処理させたいときに用いる
    これは日付date_columnをインデックスにしている。
    月~日 = 0~6
    
    :param df: urlなどを取り除きたい文章。
    :type df: data series
    :param date_column: datetimeのcolumn
    :type date_column: text
    :return: 余分なデータが取り除かれた文章
    :rtype: pandas data series
    """

    df_date = pd.DataFrame()
    df_date['year'] = df[date_column].dt.year
    df_date['month'] = df[date_column].dt.month
    df_date['weekday'] = df[date_column].dt.weekday
    df_date['day'] = df[date_column].dt.day
    df_date['hour'] = df[date_column].dt.hour
    df_date['minute'] = df[date_column].dt.minute

    return df_date


def cleaning_content(law_ds):
    """文章からurlなどの余分なデータを取り除く

    :param law_ds: urlなどを取り除きたい文章。
    :type law_ds: data series
    :return: 余分なデータが取り除かれた文章
    :rtype: pandas data series
    """

    prep_ds = law_ds.replace(r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', "", regex=True
                             ).replace(r'\n', "", regex=True
                                       ).replace(r'\r', "", regex=True
                                                 ).apply(lambda x: x.split('https://t.co')[0]
                                                         ).apply(lambda x: x.split('#Peing')[0])

    return prep_ds


def url_count(law_ds):
    """urlリンクの出現回数のカウント

    :param law_ds: urlの出現回数をカウントしたい配列
    :type law_ds: data series
    :return: url
    :rtype: pandas data series int
    """
    prep_ds = law_ds.apply(
        lambda x: len([w for w in str(x).lower().split() if 'http' in w or 'https' in w]))

    return prep_ds


def cahr_count(law_ds):
    """urlなどの余分な要素を排除したコンテンツから文字数をカウント

    :param law_ds: 文字数をカウントしたい配列
    :type law_ds: pandas data series
    :return: 文字数
    :rtype: pandas data series int
    """
    prep_ds = law_ds.replace(r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', "", regex=True
                             ).replace(r'\n', "", regex=True
                                       ).replace(r'\r', "", regex=True
                                                 ).apply(lambda x: x.split('https://t.co')[0]
                                                         ).apply(lambda x: x.split('#Peing')[0]
                                                                 ).apply(lambda x: len(x))
    return prep_ds


def hashtag_count(law_ds):
    """ハッシュタグをカウントする。ハッシュタグ以降の文字を削除しようとすると文章途中から削除されるツイートもあるため、カウントに留める

    :param law_ds: 文字数をカウントしたい配列
    :type law_ds: data series
    :return: ハッシュタグ数
    :rtype: pandas data series int
    """

    prep_ds = law_ds.apply(lambda x: len([c for c in str(x) if c == '#']))
    return prep_ds


def mention_count(law_ds):
    """メンションをカウントする。メンション以降の文字を削除しようとすると文章途中から削除されるツイートもあるため、カウントに留める

    :param law_ds: 文字数をカウントしたい配列
    :type law_ds: data series
    :return: メンション数
    :rtype: pandas data series int
    """

    prep_ds = law_ds.apply(lambda x: len([c for c in str(x) if c == '@']))
    return prep_ds


def rakuten_kugiri(law_ds):
    """
    :param law_ds: 【】で区切られた一連のレビュー文章の一連の配列
    :type law_ds: data series
    :return: 【】で区切った文章の配列を1要素とした2次元配列
    :rtype: pandas data series string
    """

    prep_ds = law_ds.apply(lambda x: re.findall("【.*?(?=【|$)", x))
    return prep_ds

