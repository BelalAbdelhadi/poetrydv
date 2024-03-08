from read_clean import *
from analyze import *

#Create instances of FileExport for each year
obj_2016 = FileClean(2016)
obj_2017 = FileClean(2017)
obj_2018 = FileClean(2018)
obj_2019 = FileClean(2019)
obj_2020 = FileClean(2020)
obj_2021 = FileClean(2021)

#Producing exported dataframes
Poetry_2016_df = obj_2016.clean_export().drop_duplicates(inplace=False)
Poetry_2017_df = obj_2017.clean_export().drop_duplicates(inplace=False)
Poetry_2018_df = obj_2018.clean_export().drop_duplicates(inplace=False)
Poetry_2019_df = obj_2019.clean_export().drop_duplicates(inplace=False)
Poetry_2020_df = obj_2020.clean_export().drop_duplicates(inplace=False)
Poetry_2021_df = obj_2021.clean_export().drop_duplicates(inplace=False)

#Exporting original dataframes
Poetry_2016_df_wo_kaur = Poetry_2016_df.query("Author != 'Rupi Kaur'")
Poetry_2017_df_wo_kaur = Poetry_2017_df.query("Author != 'Rupi Kaur'")
Poetry_2018_df_wo_kaur = Poetry_2018_df.query("Author != 'Rupi Kaur'")
Poetry_2019_df_wo_kaur = Poetry_2019_df.query("Author != 'Rupi Kaur'")
Poetry_2020_df_wo_kaur = Poetry_2020_df.query("Author != 'Rupi Kaur'")
Poetry_2021_df_wo_kaur = Poetry_2021_df.query("Author != 'Rupi Kaur'")

#Create instances of the Analyzer class
obj_2016_an = Analyzer(Poetry_2016_df, 2016)
obj_2016_an_wo_kaur = Analyzer(Poetry_2016_df_wo_kaur, 2016)
obj_2017_an = Analyzer(Poetry_2017_df, 2017)
obj_2017_an_wo_kaur = Analyzer(Poetry_2017_df_wo_kaur, 2017)
obj_2018_an = Analyzer(Poetry_2018_df, 2018)
obj_2018_an_wo_kaur = Analyzer(Poetry_2018_df_wo_kaur, 2018)
obj_2019_an = Analyzer(Poetry_2019_df, 2019)
obj_2019_an_wo_kaur = Analyzer(Poetry_2019_df_wo_kaur, 2019)
obj_2020_an = Analyzer(Poetry_2020_df, 2020)
obj_2020_an_wo_kaur = Analyzer(Poetry_2020_df_wo_kaur, 2020)
obj_2021_an = Analyzer(Poetry_2021_df, 2021)
obj_2021_an_wo_kaur = Analyzer(Poetry_2021_df_wo_kaur, 2021)

#Produce items needed for analysis

#Monthly Sales for each year 

sales_2016 = obj_2016_an.group('Month')
sales_2016_wo_kaur = obj_2016_an_wo_kaur.group('Month')
sales_2017 = obj_2017_an.group('Month')
sales_2017_wo_kaur = obj_2017_an_wo_kaur.group('Month')
sales_2018 = obj_2018_an.group('Month')
sales_2018_wo_kaur = obj_2018_an_wo_kaur.group('Month')
sales_2019 = obj_2019_an.group('Month')
sales_2019_wo_kaur = obj_2019_an_wo_kaur.group('Month')
sales_2020 = obj_2020_an.group('Month')
sales_2020_wo_kaur = obj_2020_an_wo_kaur.group('Month')
sales_2021 = obj_2021_an.group('Month')
sales_2021_wo_kaur = obj_2021_an_wo_kaur.group('Month')

#Exporting
#with Rupi Kaur
Analyzer.export(sales_2016, 'sales_2016')
Analyzer.export(sales_2017, 'sales_2017')
Analyzer.export(sales_2018, 'sales_2018')
Analyzer.export(sales_2019, 'sales_2019')
Analyzer.export(sales_2020, 'sales_2020')
Analyzer.export(sales_2021, 'sales_2021')

#without Rupi Kaur
Analyzer.export(sales_2016_wo_kaur, 'sales_2016_wo_kaur')
Analyzer.export(sales_2017_wo_kaur, 'sales_2017_wo_kaur')
Analyzer.export(sales_2018_wo_kaur, 'sales_2018_wo_kaur')
Analyzer.export(sales_2019_wo_kaur, 'sales_2019_wo_kaur')
Analyzer.export(sales_2020_wo_kaur, 'sales_2020_wo_kaur')
Analyzer.export(sales_2021_wo_kaur, 'sales_2021_wo_kaur')

#Weekly Sales for each year
sales_2016_weekly = obj_2016_an.group('Week Start')
sales_2016_weekly_wo_kaur = obj_2016_an_wo_kaur.group('Week Start')
sales_2017_weekly = obj_2017_an.group('Week Start')
sales_2017_weekly_wo_kaur = obj_2017_an_wo_kaur.group('Week Start')
sales_2018_weekly = obj_2018_an.group('Week Start')
sales_2018_weekly_wo_kaur = obj_2018_an_wo_kaur.group('Week Start')
sales_2019_weekly = obj_2019_an.group('Week Start')
sales_2019_weekly_wo_kaur = obj_2019_an_wo_kaur.group('Week Start')
sales_2020_weekly = obj_2020_an.group('Week Start')
sales_2020_weekly_wo_kaur = obj_2020_an_wo_kaur.group('Week Start')
sales_2021_weekly = obj_2021_an.group('Week Start')
sales_2021_weekly_wo_kaur = obj_2021_an_wo_kaur.group('Week Start')


#Exporting
#with Rupi Kaur
Analyzer.export(sales_2016_weekly, 'sales_2016_w')
Analyzer.export(sales_2017_weekly, 'sales_2017_w')
Analyzer.export(sales_2018_weekly, 'sales_2018_w')
Analyzer.export(sales_2019_weekly, 'sales_2019_w')
Analyzer.export(sales_2020_weekly, 'sales_2020_w')
Analyzer.export(sales_2021_weekly, 'sales_2021_w')

#withour Rupi Kaur
Analyzer.export(sales_2016_weekly_wo_kaur, 'sales_2016_w_wo_kaur')
Analyzer.export(sales_2017_weekly_wo_kaur, 'sales_2017_w_wo_kaur')
Analyzer.export(sales_2018_weekly_wo_kaur, 'sales_2018_w_wo_kaur')
Analyzer.export(sales_2019_weekly_wo_kaur, 'sales_2019_w_wo_kaur')
Analyzer.export(sales_2020_weekly_wo_kaur, 'sales_2020_w_wo_kaur')
Analyzer.export(sales_2021_weekly_wo_kaur, 'sales_2021_w_wo_kaur')

#Weekly sales for comparison
#with Rupi Kaur
sales_2016_weekly_yc = obj_2016_an.group('Week No.').sort_values('Week No.')
sales_2017_weekly_yc = obj_2017_an.group('Week No.').sort_values('Week No.')
sales_2018_weekly_yc = obj_2018_an.group('Week No.').sort_values('Week No.')
sales_2019_weekly_yc = obj_2019_an.group('Week No.').sort_values('Week No.')
sales_2020_weekly_yc = obj_2020_an.group('Week No.').sort_values('Week No.')
sales_2021_weekly_yc = obj_2021_an.group('Week No.').sort_values('Week No.')

#without Rupi Kaur
sales_2016_weekly_yc_wo_kaur = obj_2016_an_wo_kaur.group('Week No.').sort_values('Week No.')
sales_2017_weekly_yc_wo_kaur = obj_2017_an_wo_kaur.group('Week No.').sort_values('Week No.')
sales_2018_weekly_yc_wo_kaur = obj_2018_an_wo_kaur.group('Week No.').sort_values('Week No.')
sales_2019_weekly_yc_wo_kaur = obj_2019_an_wo_kaur.group('Week No.').sort_values('Week No.')
sales_2020_weekly_yc_wo_kaur = obj_2020_an_wo_kaur.group('Week No.').sort_values('Week No.')
sales_2021_weekly_yc_wo_kaur = obj_2021_an_wo_kaur.group('Week No.').sort_values('Week No.')

#Exporting
Analyzer.export(sales_2016_weekly_yc, 'sales_2016_weekly_yc')
Analyzer.export(sales_2017_weekly_yc, 'sales_2017_weekly_yc')
Analyzer.export(sales_2018_weekly_yc, 'sales_2018_weekly_yc')
Analyzer.export(sales_2019_weekly_yc, 'sales_2019_weekly_yc')
Analyzer.export(sales_2020_weekly_yc, 'sales_2020_weekly_yc')
Analyzer.export(sales_2021_weekly_yc, 'sales_2021_weekly_yc')

Analyzer.export(sales_2016_weekly_yc_wo_kaur, 'sales_2016_weekly_yc_wo_kaur')
Analyzer.export(sales_2017_weekly_yc_wo_kaur, 'sales_2017_weekly_yc_wo_kaur')
Analyzer.export(sales_2018_weekly_yc_wo_kaur, 'sales_2018_weekly_yc_wo_kaur')
Analyzer.export(sales_2019_weekly_yc_wo_kaur, 'sales_2019_weekly_yc_wo_kaur')
Analyzer.export(sales_2020_weekly_yc_wo_kaur, 'sales_2020_weekly_yc_wo_kaur')
Analyzer.export(sales_2021_weekly_yc_wo_kaur, 'sales_2021_weekly_yc_wo_kaur')


#Top Authors and books

"""#2016
top_5_authors_2016 = obj_2016_an.top('Author', 5)
top_10_authors_2016 = obj_2016_an.top('Author', 10)
top_5_books_2016 = obj_2016_an.top('Title', 5)
top_10_books_2016 = obj_2016_an.top('Title', 10)

#2017
top_5_authors_2017 = obj_2017_an.top('Author', 5)
top_10_authors_2017 = obj_2017_an.top('Author', 10)
top_5_books_2017 = obj_2017_an.top('Title', 5)
top_10_books_2017 = obj_2017_an.top('Title', 10)

#2018
top_5_authors_2018 = obj_2018_an.top('Author', 5)
top_10_authors_2018 = obj_2018_an.top('Author', 10)
top_5_books_2018 = obj_2018_an.top('Title', 5)
top_10_books_2018 = obj_2018_an.top('Title', 10)

#2019
top_5_authors_2019 = obj_2019_an.top('Author', 5)
top_10_authors_2019 = obj_2019_an.top('Author', 10)
top_5_books_2019 = obj_2019_an.top('Title', 5)
top_10_books_2019 = obj_2019_an.top('Title', 10)

#2020
top_5_authors_2020 = obj_2020_an.top('Author', 5)
top_10_authors_2020 = obj_2020_an.top('Author', 10)
top_5_books_2020 = obj_2020_an.top('Title', 5)
top_10_books_2020 = obj_2020_an.top('Title', 10)

#2021
top_5_authors_2021 = obj_2021_an.top('Author', 5)
top_10_authors_2021 = obj_2021_an.top('Author', 10)
top_5_books_2021 = obj_2021_an.top('Title', 5)
top_10_books_2021 = obj_2021_an.top('Title', 10)"""

#Market Shares
#2016 with Rupi Kaur
shares_5_authors_2016 = obj_2016_an.market_share('Author', 5)
shares_10_authors_2016 = obj_2016_an.market_share('Author', 10)
shares_5_books_2016 = obj_2016_an.market_share('Title', 5)
shares_10_books_2016 = obj_2016_an.market_share('Title', 10)

#2016 without Rupi Kaur
shares_5_authors_2016_wo_kaur = obj_2016_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2016_wo_kaur = obj_2016_an_wo_kaur.market_share('Author', 10)
shares_5_books_2016_wo_kaur = obj_2016_an_wo_kaur.market_share('Title', 5)
shares_10_books_2016_wo_kaur = obj_2016_an_wo_kaur.market_share('Title', 10)

#Exporting
Analyzer.export(shares_10_authors_2016, 'shares_2016_auth10')
Analyzer.export(shares_10_books_2016, 'shares_2016_book10')
Analyzer.export(shares_5_authors_2016, 'shares_2016_auth5')
Analyzer.export(shares_5_books_2016, 'shares_2016_book5')
Analyzer.export(shares_10_authors_2016_wo_kaur, 'shares_2016_auth10_wo_kaur')
Analyzer.export(shares_10_books_2016_wo_kaur, 'shares_2016_book10_wo_kaur')
Analyzer.export(shares_5_authors_2016_wo_kaur, 'shares_2016_auth5_wo_kaur')
Analyzer.export(shares_5_books_2016_wo_kaur, 'shares_2016_book5_wo_kaur')

#2017 with Rupi Kaur
shares_5_authors_2017 = obj_2017_an.market_share('Author', 5)
shares_10_authors_2017 = obj_2017_an.market_share('Author', 10)
shares_5_books_2017 = obj_2017_an.market_share('Title', 5)
shares_10_books_2017 = obj_2017_an.market_share('Title', 10)

#2017 without Rupi Kaur
shares_5_authors_2017_wo_kaur = obj_2017_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2017_wo_kaur = obj_2017_an_wo_kaur.market_share('Author', 10)
shares_5_books_2017_wo_kaur = obj_2017_an_wo_kaur.market_share('Title', 5)
shares_10_books_2017_wo_kaur = obj_2017_an_wo_kaur.market_share('Title', 10)

#Exporting
Analyzer.export(shares_10_authors_2017, 'shares_2017_auth10')
Analyzer.export(shares_10_books_2017, 'shares_2017_book10')
Analyzer.export(shares_5_authors_2017, 'shares_2017_auth5')
Analyzer.export(shares_5_books_2017, 'shares_2017_book5')
Analyzer.export(shares_10_authors_2017_wo_kaur, 'shares_2017_auth10_wo_kaur')
Analyzer.export(shares_10_books_2017_wo_kaur, 'shares_2017_book10_wo_kaur')
Analyzer.export(shares_5_authors_2017_wo_kaur, 'shares_2017_auth5_wo_kaur')
Analyzer.export(shares_5_books_2017_wo_kaur, 'shares_2017_book5_wo_kaur')

#2018 with Rupi Kaur
shares_5_authors_2018 = obj_2018_an.market_share('Author', 5)
shares_10_authors_2018 = obj_2018_an.market_share('Author', 10)
shares_5_books_2018 = obj_2018_an.market_share('Title', 5)
shares_10_books_2018 = obj_2018_an.market_share('Title', 10)

#2018 without Rupi Kaur
shares_5_authors_2018_wo_kaur = obj_2018_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2018_wo_kaur = obj_2018_an_wo_kaur.market_share('Author', 10)
shares_5_books_2018_wo_kaur = obj_2018_an_wo_kaur.market_share('Title', 5)
shares_10_books_2018_wo_kaur = obj_2018_an_wo_kaur.market_share('Title', 10)

#Exporting
Analyzer.export(shares_10_authors_2018, 'shares_2018_auth10')
Analyzer.export(shares_10_books_2018, 'shares_2018_book10')
Analyzer.export(shares_5_authors_2018, 'shares_2018_auth5')
Analyzer.export(shares_5_books_2018, 'shares_2018_book5')
Analyzer.export(shares_10_authors_2018_wo_kaur, 'shares_2018_auth10_wo_kaur')
Analyzer.export(shares_10_books_2018_wo_kaur, 'shares_2018_book10_wo_kaur')
Analyzer.export(shares_5_authors_2018_wo_kaur, 'shares_2018_auth5_wo_kaur')
Analyzer.export(shares_5_books_2018_wo_kaur, 'shares_2018_book5_wo_kaur')

#2019
shares_5_authors_2019 = obj_2019_an.market_share('Author', 5)
shares_10_authors_2019 = obj_2019_an.market_share('Author', 10)
shares_5_books_2019 = obj_2019_an.market_share('Title', 5)
shares_10_books_2019 = obj_2019_an.market_share('Title', 10)

#2019 without Rupi Kaur
shares_5_authors_2019_wo_kaur = obj_2019_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2019_wo_kaur = obj_2019_an_wo_kaur.market_share('Author', 10)
shares_5_books_2019_wo_kaur = obj_2019_an_wo_kaur.market_share('Title', 5)
shares_10_books_2019_wo_kaur = obj_2019_an_wo_kaur.market_share('Title', 10)

#Exporting 
Analyzer.export(shares_10_authors_2019, 'shares_2019_auth10')
Analyzer.export(shares_10_books_2019, 'shares_2019_book10')
Analyzer.export(shares_5_authors_2019, 'shares_2019_auth5')
Analyzer.export(shares_5_books_2019, 'shares_2019_book5')
Analyzer.export(shares_10_authors_2019_wo_kaur, 'shares_2019_auth10_wo_kaur')
Analyzer.export(shares_10_books_2019_wo_kaur, 'shares_2019_book10_wo_kaur')
Analyzer.export(shares_5_authors_2019_wo_kaur, 'shares_2019_auth5_wo_kaur')
Analyzer.export(shares_5_books_2019_wo_kaur, 'shares_2019_book5_wo_kaur')

#2020
shares_5_authors_2020 = obj_2020_an.market_share('Author', 5)
shares_10_authors_2020 = obj_2020_an.market_share('Author', 10)
shares_5_books_2020 = obj_2020_an.market_share('Title', 5)
shares_10_books_2020 = obj_2020_an.market_share('Title', 10)

#2020 without Rupi Kaur
shares_5_authors_2020_wo_kaur = obj_2020_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2020_wo_kaur = obj_2020_an_wo_kaur.market_share('Author', 10)
shares_5_books_2020_wo_kaur = obj_2020_an_wo_kaur.market_share('Title', 5)
shares_10_books_2020_wo_kaur = obj_2020_an_wo_kaur.market_share('Title', 10)

#Exporting
Analyzer.export(shares_10_authors_2020, 'shares_2020_auth10')
Analyzer.export(shares_10_books_2020, 'shares_2020_book10')
Analyzer.export(shares_5_authors_2020, 'shares_2020_auth5')
Analyzer.export(shares_5_books_2020, 'shares_2020_book5')
Analyzer.export(shares_10_authors_2020_wo_kaur, 'shares_2020_auth10_wo_kaur')
Analyzer.export(shares_10_books_2020_wo_kaur, 'shares_2020_book10_wo_kaur')
Analyzer.export(shares_5_authors_2020_wo_kaur, 'shares_2020_auth5_wo_kaur')
Analyzer.export(shares_5_books_2020_wo_kaur, 'shares_2020_book5_wo_kaur')

#2021
shares_5_authors_2021 = obj_2021_an.market_share('Author', 5)
shares_10_authors_2021 = obj_2021_an.market_share('Author', 10)
shares_5_books_2021 = obj_2021_an.market_share('Title', 5)
shares_10_books_2021 = obj_2021_an.market_share('Title', 10)

#2021 without Rupi Kaur
shares_5_authors_2021_wo_kaur = obj_2021_an_wo_kaur.market_share('Author', 5)
shares_10_authors_2021_wo_kaur = obj_2021_an_wo_kaur.market_share('Author', 10)
shares_5_books_2021_wo_kaur = obj_2021_an_wo_kaur.market_share('Title', 5)
shares_10_books_2021_wo_kaur = obj_2021_an_wo_kaur.market_share('Title', 10)

#Exporting
Analyzer.export(shares_10_authors_2021, 'shares_2021_auth10')
Analyzer.export(shares_10_books_2021, 'shares_2021_book10')
Analyzer.export(shares_5_authors_2021, 'shares_2021_auth5')
Analyzer.export(shares_5_books_2021, 'shares_2021_book5')
Analyzer.export(shares_10_authors_2021_wo_kaur, 'shares_2021_auth10_wo_kaur')
Analyzer.export(shares_10_books_2021_wo_kaur, 'shares_2021_book10_wo_kaur')
Analyzer.export(shares_5_authors_2021_wo_kaur, 'shares_2021_auth5_wo_kaur')
Analyzer.export(shares_5_books_2021_wo_kaur, 'shares_2021_book5_wo_kaur')

#2021_vs_avg monthly
#With Rupi Kaur
avg_sales = []
list_of_df = [Poetry_2017_df, Poetry_2018_df, Poetry_2019_df, Poetry_2020_df]

for idx, val in enumerate(list_of_df):
    avg_year = val.groupby('Month').sum()
    avg_year = avg_year['TW Sales']
    avg_year.rename('Total Sales', inplace=True)
    avg_sales.append(avg_year)
avg_sales = pd.DataFrame(avg_sales)
sales_2021_avg = pd.DataFrame([avg_sales.mean(), sales_2021['Total Sales']])
sales_2021_avg.index = ['Average Sales', '2021 Sales']

Analyzer.export(sales_2021_avg, 'sales_2021_performance')

#Without Rupi Kaur
avg_sales_wo_kaur = []
list_of_df_wo_kaur = [
                    Poetry_2017_df_wo_kaur,
                    Poetry_2018_df_wo_kaur,
                    Poetry_2019_df_wo_kaur,
                    Poetry_2020_df_wo_kaur,
                    Poetry_2021_df_wo_kaur]
for idx, val in enumerate(list_of_df_wo_kaur):
    avg_year = val.groupby('Month').sum()
    avg_year = avg_year['TW Sales']
    avg_year.rename('Total Sales', inplace=True)
    avg_sales_wo_kaur.append(avg_year)
avg_sales_wo_kaur = pd.DataFrame(avg_sales_wo_kaur)
sales_2021_avg_wo_kaur = pd.DataFrame([avg_sales_wo_kaur.mean(), sales_2021_wo_kaur['Total Sales']])
sales_2021_avg_wo_kaur.index = ['Average Sales', '2021 Sales']
Analyzer.export(sales_2021_avg_wo_kaur, 'sales_2021_performance_wo_kaur')


#2021_vs_avg_weekly
avg_w_sales = []
for idx, val in enumerate(list_of_df):
    avg_year = val.groupby('Week No.').sum()
    avg_year = avg_year['TW Sales']
    avg_year.rename('Total Sales', inplace=True)
    avg_w_sales.append(avg_year)
avg_w_sales = pd.DataFrame(avg_w_sales)
sales_2021_weekly_per = Poetry_2021_df.groupby('Week No.').sum()
sales_2021_weekly_per = sales_2021_weekly_per['TW Sales']
#sales_2021_weekly_per.rename('Total Sales', inplace=True)
sales_2021_avg_w = pd.DataFrame([avg_w_sales.mean(), sales_2021_weekly_per])
sales_2021_avg_w.index = ['Average Sales', '2021 Sales']
Analyzer.export(sales_2021_avg_w, 'sales_2021_performance_w')

#2021_vs_avg_weekly
avg_w_sales_wo_kaur = []
for idx, val in enumerate(list_of_df_wo_kaur):
    avg_year = val.groupby('Week No.').sum()
    avg_year = avg_year['TW Sales']
    avg_year.rename('Total Sales', inplace=True)
    avg_w_sales_wo_kaur.append(avg_year)
avg_w_sales_wo_kaur = pd.DataFrame(avg_w_sales_wo_kaur)
sales_2021_weekly_per_wo_kaur = Poetry_2021_df_wo_kaur.groupby('Week No.').sum()
sales_2021_weekly_per_wo_kaur = sales_2021_weekly_per_wo_kaur['TW Sales']
#sales_2021_weekly_per.rename('Total Sales', inplace=True)
sales_2021_avg_w_wo_kaur = pd.DataFrame([avg_w_sales_wo_kaur.mean(), sales_2021_weekly_per_wo_kaur])
sales_2021_avg_w_wo_kaur.index = ['Average Sales', '2021 Sales']
Analyzer.export(sales_2021_avg_w_wo_kaur, 'sales_2021_performance_w_wo_kaur')
