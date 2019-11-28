#.sql模板测试
```
SELECT * FROM public.pointpool 
WHERE pointid = '{{field1}}' AND version = {{field2}};   
```
`http://127.0.0.1:6000/_QUERIES/foo/some_get?field1=2bceef38-634a-11e8-9a2d-1b370b934e93&field2=2` 
 
-
```
SELECT * FROM public.pointpool
{% if field1 %}WHERE pointid = '{{field1}}'{% endif %};
```
`http://127.0.0.1:6000/_QUERIES/foo/some_get2?field1=2bceef38-634a-11e8-9a2d-1b370b934e93` 

-
```
SELECT * FROM public.pointpool
WHERE pointid = '{{ field1 | default('2bceef38-634a-11e8-9a2d-1b370b934e93', true) }}';
```
`http://127.0.0.1:6000/_QUERIES/foo/some_get3?field1=2bceef38-634a-11e8-9a2d-1b370b934e93` 

 

#uri测试
###?_select 

`http://127.0.0.1:6000/event_tracking/public/pointpool?_select=version` 
 
-
###?_count

`http://127.0.0.1:6000/event_tracking/public/pointpool?_count=pointid` 
 
-
###?_page

`http://127.0.0.1:6000/event_tracking/public/pointpool?_select=page_name&_page=2&_page_size=8` 
 
-
###?_join

`http://127.0.0.1:6000/event_tracking/public/pointpool a?_join=INNER:pointpool b:a.pointid:eq:b.pointid` 
 
-