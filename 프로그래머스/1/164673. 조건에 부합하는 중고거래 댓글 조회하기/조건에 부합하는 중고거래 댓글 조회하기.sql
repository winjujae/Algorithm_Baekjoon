SELECT a.title, a.board_id, b.reply_id, b.writer_id, b.contents
    , to_char(b.created_date, 'yyyy-mm-dd') as created_date
from used_goods_board a
inner join used_goods_reply b on a.board_id = b.board_id
where to_char(a.created_date,'yyyy-mm') = '2022-10'
order by created_date asc, a.title asc