use pubs;
select pubs.pub_name as Publishers, titles.title as Title, titleauthor.au_id as AuthID, authors.au_fname as Firstname, pubs.authors.au_lname Lastname
from pubs.publishers pubs 
inner join pubs.titles titles
	on pubs.pub_id = titles.pub_id
inner join pubs.titleauthor titleauthor
    on titles.title_id = titleauthor.title_id
inner join pubs.authors authors
    on titleauthor.au_id = authors.au_id;

select pubs.pub_name as Publishers, count(titles.title) as Title, titleauthor.au_id as AuthID, authors.au_fname as Firstname, pubs.authors.au_lname Lastname
from pubs.publishers pubs 
inner join pubs.titles titles
	on pubs.pub_id = titles.pub_id
inner join pubs.titleauthor titleauthor
    on titles.title_id = titleauthor.title_id
inner join pubs.authors authors
    on titleauthor.au_id = authors.au_id
group by title;