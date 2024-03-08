import pandas as pd
import plotly.graph_objs as go

#Reading the dataframes:
#With Rupi Kaur
#Monthly sales
sales_2016 = pd.read_csv('export/2016/sales_2016', index_col='Month')
sales_2017 = pd.read_csv('export/2017/sales_2017', index_col='Month')
sales_2018 = pd.read_csv('export/2018/sales_2018', index_col='Month')
sales_2019 = pd.read_csv('export/2019/sales_2019', index_col='Month')
sales_2020 = pd.read_csv('export/2020/sales_2020', index_col='Month')
sales_2021 = pd.read_csv('export/2021/sales_2021', index_col='Month')
#Without Rupi Kaur
sales_2016_wo_kaur = pd.read_csv('export/2016/sales_2016_wo_kaur', index_col='Month')
sales_2017_wo_kaur = pd.read_csv('export/2017/sales_2017_wo_kaur', index_col='Month')
sales_2018_wo_kaur = pd.read_csv('export/2018/sales_2018_wo_kaur', index_col='Month')
sales_2019_wo_kaur = pd.read_csv('export/2019/sales_2019_wo_kaur', index_col='Month')
sales_2020_wo_kaur = pd.read_csv('export/2020/sales_2020_wo_kaur', index_col='Month')
sales_2021_wo_kaur = pd.read_csv('export/2021/sales_2021_wo_kaur', index_col='Month')

#Weekly sales
#With Rupi Kaur
sales_2016_weekly = pd.read_csv('export/2016/sales_2016_w', index_col='Week Start')
sales_2017_weekly = pd.read_csv('export/2017/sales_2017_w', index_col='Week Start')
sales_2018_weekly = pd.read_csv('export/2018/sales_2018_w', index_col='Week Start')
sales_2019_weekly = pd.read_csv('export/2019/sales_2019_w', index_col='Week Start')
sales_2020_weekly = pd.read_csv('export/2020/sales_2020_w', index_col='Week Start')
sales_2021_weekly = pd.read_csv('export/2021/sales_2021_w', index_col='Week Start')

#Without Rupi Kaur
sales_2016_weekly_wo_kaur = pd.read_csv('export/2016/sales_2016_w_wo_kaur', index_col='Week Start')
sales_2017_weekly_wo_kaur = pd.read_csv('export/2017/sales_2017_w_wo_kaur', index_col='Week Start')
sales_2018_weekly_wo_kaur = pd.read_csv('export/2018/sales_2018_w_wo_kaur', index_col='Week Start')
sales_2019_weekly_wo_kaur = pd.read_csv('export/2019/sales_2019_w_wo_kaur', index_col='Week Start')
sales_2020_weekly_wo_kaur = pd.read_csv('export/2020/sales_2020_w_wo_kaur', index_col='Week Start')
sales_2021_weekly_wo_kaur = pd.read_csv('export/2021/sales_2021_w_wo_kaur', index_col='Week Start')


#Weekly sales for comparison
#With Rupi Kaur
sales_2016_weekly_yc = pd.read_csv('export/2016/sales_2016_weekly_yc', index_col='Week No.')
sales_2017_weekly_yc = pd.read_csv('export/2017/sales_2017_weekly_yc', index_col='Week No.')
sales_2018_weekly_yc = pd.read_csv('export/2018/sales_2018_weekly_yc', index_col='Week No.')
sales_2019_weekly_yc = pd.read_csv('export/2019/sales_2019_weekly_yc', index_col='Week No.')
sales_2020_weekly_yc = pd.read_csv('export/2020/sales_2020_weekly_yc', index_col='Week No.')
sales_2021_weekly_yc = pd.read_csv('export/2021/sales_2021_weekly_yc', index_col='Week No.')

#Without Rupi Kaur
sales_2016_weekly_yc_wo_kaur = pd.read_csv('export/2016/sales_2016_weekly_yc_wo_kaur', index_col = 'Week No.')
sales_2017_weekly_yc_wo_kaur = pd.read_csv('export/2017/sales_2017_weekly_yc_wo_kaur', index_col = 'Week No.')
sales_2018_weekly_yc_wo_kaur = pd.read_csv('export/2018/sales_2018_weekly_yc_wo_kaur', index_col = 'Week No.')
sales_2019_weekly_yc_wo_kaur = pd.read_csv('export/2019/sales_2019_weekly_yc_wo_kaur', index_col = 'Week No.')
sales_2020_weekly_yc_wo_kaur = pd.read_csv('export/2020/sales_2020_weekly_yc_wo_kaur', index_col = 'Week No.')
sales_2021_weekly_yc_wo_kaur = pd.read_csv('export/2021/sales_2021_weekly_yc_wo_kaur', index_col = 'Week No.')

#Top 10 authors
#With Rupi Kaur
shares_10_authors_2016 = pd.read_csv('export/2016/shares_2016_auth10', index_col = 0)
shares_10_authors_2017 = pd.read_csv('export/2017/shares_2017_auth10', index_col = 0)
shares_10_authors_2018 = pd.read_csv('export/2018/shares_2018_auth10', index_col = 0)
shares_10_authors_2019 = pd.read_csv('export/2019/shares_2019_auth10', index_col = 0)
shares_10_authors_2020 = pd.read_csv('export/2020/shares_2020_auth10', index_col = 0)
shares_10_authors_2021 = pd.read_csv('export/2021/shares_2021_auth10', index_col = 0)
#Without Rupi Kaur
shares_10_authors_2016_wo_kaur = pd.read_csv('export/2016/shares_2016_auth10_wo_kaur', index_col=0)
shares_10_authors_2017_wo_kaur = pd.read_csv('export/2017/shares_2017_auth10_wo_kaur', index_col=0)
shares_10_authors_2018_wo_kaur = pd.read_csv('export/2018/shares_2018_auth10_wo_kaur', index_col=0)
shares_10_authors_2019_wo_kaur = pd.read_csv('export/2019/shares_2019_auth10_wo_kaur', index_col=0)
shares_10_authors_2020_wo_kaur = pd.read_csv('export/2020/shares_2020_auth10_wo_kaur', index_col=0)
shares_10_authors_2021_wo_kaur = pd.read_csv('export/2021/shares_2021_auth10_wo_kaur', index_col=0)


#Top 5 authors
#With Rupi Kaur
shares_5_authors_2016 = pd.read_csv('export/2016/shares_2016_auth5', index_col = 0)
shares_5_authors_2017 = pd.read_csv('export/2017/shares_2017_auth5', index_col = 0)
shares_5_authors_2018 = pd.read_csv('export/2018/shares_2018_auth5', index_col = 0)
shares_5_authors_2019 = pd.read_csv('export/2019/shares_2019_auth5', index_col = 0)
shares_5_authors_2020 = pd.read_csv('export/2020/shares_2020_auth5', index_col = 0)
shares_5_authors_2021 = pd.read_csv('export/2021/shares_2021_auth5', index_col = 0)

#Without Rupi Kaur
shares_5_authors_2016_wo_kaur = pd.read_csv('export/2016/shares_2016_auth5_wo_kaur', index_col=0)
shares_5_authors_2017_wo_kaur = pd.read_csv('export/2017/shares_2017_auth5_wo_kaur', index_col=0)
shares_5_authors_2018_wo_kaur = pd.read_csv('export/2018/shares_2018_auth5_wo_kaur', index_col=0)
shares_5_authors_2019_wo_kaur = pd.read_csv('export/2019/shares_2019_auth5_wo_kaur', index_col=0)
shares_5_authors_2020_wo_kaur = pd.read_csv('export/2020/shares_2020_auth5_wo_kaur', index_col=0)
shares_5_authors_2021_wo_kaur = pd.read_csv('export/2021/shares_2021_auth5_wo_kaur', index_col=0)


#Top 10 books
#With Rupi Kaur
shares_10_books_2016 = pd.read_csv('export/2016/shares_2016_book10', index_col = 0)
shares_10_books_2017 = pd.read_csv('export/2017/shares_2017_book10', index_col = 0)
shares_10_books_2018 = pd.read_csv('export/2018/shares_2018_book10', index_col = 0)
shares_10_books_2019 = pd.read_csv('export/2019/shares_2019_book10', index_col = 0)
shares_10_books_2020 = pd.read_csv('export/2020/shares_2020_book10', index_col = 0)
shares_10_books_2021 = pd.read_csv('export/2021/shares_2021_book10', index_col = 0)

#Without Rupi Kaur
shares_10_books_2016_wo_kaur = pd.read_csv('export/2016/shares_2016_book10_wo_kaur', index_col=0)
shares_10_books_2017_wo_kaur = pd.read_csv('export/2017/shares_2017_book10_wo_kaur', index_col=0)
shares_10_books_2018_wo_kaur = pd.read_csv('export/2018/shares_2018_book10_wo_kaur', index_col=0)
shares_10_books_2019_wo_kaur = pd.read_csv('export/2019/shares_2019_book10_wo_kaur', index_col=0)
shares_10_books_2020_wo_kaur = pd.read_csv('export/2020/shares_2020_book10_wo_kaur', index_col=0)
shares_10_books_2021_wo_kaur = pd.read_csv('export/2021/shares_2021_book10_wo_kaur', index_col=0)

#Top 5 books
#With Rupi Kaur
shares_5_books_2016 = pd.read_csv('export/2016/shares_2016_book5', index_col=0)
shares_5_books_2017 = pd.read_csv('export/2017/shares_2017_book5', index_col=0)
shares_5_books_2018 = pd.read_csv('export/2018/shares_2018_book5', index_col=0)
shares_5_books_2019 = pd.read_csv('export/2019/shares_2019_book5', index_col=0)
shares_5_books_2020 = pd.read_csv('export/2020/shares_2020_book5', index_col=0)
shares_5_books_2021 = pd.read_csv('export/2021/shares_2021_book5', index_col=0)

#Without Rupi Kaur
shares_5_books_2016_wo_kaur = pd.read_csv('export/2016/shares_2016_book5_wo_kaur', index_col=0)
shares_5_books_2017_wo_kaur = pd.read_csv('export/2017/shares_2017_book5_wo_kaur', index_col=0)
shares_5_books_2018_wo_kaur = pd.read_csv('export/2018/shares_2018_book5_wo_kaur', index_col=0)
shares_5_books_2019_wo_kaur = pd.read_csv('export/2019/shares_2019_book5_wo_kaur', index_col=0)
shares_5_books_2020_wo_kaur = pd.read_csv('export/2020/shares_2020_book5_wo_kaur', index_col=0)
shares_5_books_2021_wo_kaur = pd.read_csv('export/2021/shares_2021_book5_wo_kaur', index_col=0)



sales = { 
        'rupi_kaur':{
            'Monthly': {
            
                2016: sales_2016,
                2017: sales_2017,
                2018: sales_2018, 
                2019: sales_2019, 
                2020: sales_2020, 
                2021: sales_2021},
            
            'Weekly': {
                2016: sales_2016_weekly,
                2017: sales_2017_weekly,
                2018: sales_2018_weekly,
                2019: sales_2019_weekly,
                2020: sales_2020_weekly,
                2021: sales_2021_weekly}},
        
        '!rupi_kaur':{
            'Monthly':{
                2016: sales_2016_wo_kaur,
                2017: sales_2017_wo_kaur,
                2018: sales_2018_wo_kaur,
                2019: sales_2019_wo_kaur,
                2020: sales_2020_wo_kaur,
                2021: sales_2021_wo_kaur},
            'Weekly':{
                2016: sales_2016_weekly_wo_kaur,
                2017: sales_2017_weekly_wo_kaur,
                2018: sales_2018_weekly_wo_kaur,
                2019: sales_2019_weekly_wo_kaur,
                2020: sales_2020_weekly_wo_kaur,
                2021: sales_2021_weekly_wo_kaur
            }}}

sales_weekly_yc = {
    'rupi_kaur': {
        2016:sales_2016_weekly_yc,
        2017:sales_2017_weekly_yc,
        2018:sales_2018_weekly_yc,
        2019:sales_2019_weekly_yc,
        2020:sales_2020_weekly_yc,
        2021:sales_2021_weekly_yc
    },
    '!rupi_kaur': {
        2016:sales_2016_weekly_yc_wo_kaur,
        2017:sales_2017_weekly_yc_wo_kaur,
        2018:sales_2018_weekly_yc_wo_kaur,
        2019:sales_2019_weekly_yc_wo_kaur,
        2020:sales_2020_weekly_yc_wo_kaur,
        2021:sales_2021_weekly_yc_wo_kaur
    }
}




market_shares = {
'rupi_kaur': {
    'Author': {
            'Top 10': {
                2016: shares_10_authors_2016,
                2017: shares_10_authors_2017,
                2018: shares_10_authors_2018,
                2019: shares_10_authors_2019,
                2020: shares_10_authors_2020,
                2021: shares_10_authors_2021
            },
            'Top 5': {
                2016: shares_5_authors_2016,
                2017: shares_5_authors_2017,
                2018: shares_5_authors_2018,
                2019: shares_5_authors_2019,
                2020: shares_5_authors_2020,
                2021: shares_5_authors_2021
            }
    },
    'Title': {
        'Top 10': {
            2016: shares_10_books_2016,
            2017: shares_10_books_2017,
            2018: shares_10_books_2018,
            2019: shares_10_books_2019,
            2020: shares_10_books_2020,
            2021: shares_10_books_2021
        },
        'Top 5': {
            2016: shares_5_books_2016,
            2017: shares_5_books_2017,
            2018: shares_5_books_2018,
            2019: shares_5_books_2019,
            2020: shares_5_books_2020,
            2021: shares_5_books_2021
        }
    }
},
'!rupi_kaur': {
    'Author': {
            'Top 10': {
                2016: shares_10_authors_2016_wo_kaur,
                2017: shares_10_authors_2017_wo_kaur,
                2018: shares_10_authors_2018_wo_kaur,
                2019: shares_10_authors_2019_wo_kaur,
                2020: shares_10_authors_2020_wo_kaur,
                2021: shares_10_authors_2021_wo_kaur
            },
            'Top 5': {
                2016: shares_5_authors_2016_wo_kaur,
                2017: shares_5_authors_2017_wo_kaur,
                2018: shares_5_authors_2018_wo_kaur,
                2019: shares_5_authors_2019_wo_kaur,
                2020: shares_5_authors_2020_wo_kaur,
                2021: shares_5_authors_2021_wo_kaur
            }
    },
    'Title': {
        'Top 10': {
            2016: shares_10_books_2016_wo_kaur,
            2017: shares_10_books_2017_wo_kaur,
            2018: shares_10_books_2018_wo_kaur,
            2019: shares_10_books_2019_wo_kaur,
            2020: shares_10_books_2020_wo_kaur,
            2021: shares_10_books_2021_wo_kaur
        },
        'Top 5': {
            2016: shares_5_books_2016_wo_kaur,
            2017: shares_5_books_2017_wo_kaur,
            2018: shares_5_books_2018_wo_kaur,
            2019: shares_5_books_2019_wo_kaur,
            2020: shares_5_books_2020_wo_kaur,
            2021: shares_5_books_2021_wo_kaur
        }
    }
}
}

#Misc
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales_2021_vs_avg_with_kaur = pd.read_csv('export/2021/sales_2021_performance', index_col = 0)
sales_2021_vs_avg_wo_kaur = pd.read_csv('export/2021/sales_2021_performance_wo_kaur', index_col=0)

sales_2021_vs_avg ={ 
    'rupi_kaur': sales_2021_vs_avg_with_kaur,
    '!rupi_kaur': sales_2021_vs_avg_wo_kaur
} 
sales_2021_vs_avg_w = pd.read_csv('export/2021/sales_2021_performance_w')
sales_2021_vs_avg_w_wo_kaur = pd.read_csv('export/2021/sales_2021_performance_w_wo_kaur')

sales_2021_vs_avg_weekly = {
    'rupi_kaur': sales_2021_vs_avg_w,
    '!rupi_kaur': sales_2021_vs_avg_w_wo_kaur
}

weeks = [f'Week {i}' for i in range(1,54)]