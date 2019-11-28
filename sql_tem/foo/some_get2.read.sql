SELECT * FROM public.pointpool
{% if field1 %}WHERE pointid = '{{field1}}'{% endif %}
