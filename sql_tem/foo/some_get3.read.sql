SELECT * FROM public.pointpool
WHERE pointid = '{{ field1 | default('2bceef38-634a-11e8-9a2d-1b370b934e93', true) }}'
;