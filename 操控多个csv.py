import pandas as pd
to_read = pd.read_csv("to_read.csv")
to_read_counts = to_read['book_id'].value_counts().sort_value(ascending=False)
hottest_50_books_id = to_read_counts[:50].index
hottest_50_books_counts = to_read_counts[:50].values
hottest_50_books = pd.DataFrame(
    {'book_id':hottest_50_books_id,'to_read_counts':hottest_50_books_counts}
)
print(hottest_50_books)
books = pd.read_csv("books.csv")
book_id_and_title = books[['book_id',"goodreads_book_id",'title']]
hottest_50_books_with_title = pd.merge(
    hottest_50_books,book_id_and_title,on='book_id',how='left'
)
print(hottest_50_books_with_title)
hottest_50_books_with_title.to_csv('./output/hottest_50_books_with_title.csv')
book_tags = pd.read_csv('book_tags.csv')
book_tags = book_tags[
    book_tags['_goodreads_book_id_'].isin(
        hottest_50_books_with_title['goodreads_book_id']
    )
]
del book_tags['_goodreads_book_id_']
hottest_10_tags = book_tags.groupby('tag_id').sum()
hottest_10_tags = hottest_10_tags.sort_values(by='count',ascending=False)[:10]
print(hottest_10_tags)
tags = pd.read_csv('tags.csv')
hottest_10_tags_with_tag_name = pd.merge(hottest_10_tags,tags,on='tag_id',how='left')
print(hottest_10_tags_with_tag_name)
hottest_10_tags_with_tag_name.to_csv('./output/hottest_10_tags_with_tag_name.csv')