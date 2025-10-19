---
layout: default
title: Reports of Latest AI Papers
---

# Recent Papers Reports

{% assign sorted_files = site.data.markdown_files %}
{% assign current_month_key = site.time | date: "%Y-%m" %}
{% assign grouped_by_month = sorted_files | group_by_exp: "file", "file.title | slice: 0, 7" %}
{% assign sorted_groups = grouped_by_month | sort: "name" | reverse %}

{% assign current_month_group = sorted_groups | where: "name", current_month_key | first %}
{% assign previous_year = nil %}
{% if current_month_group %}
<details open>
  <summary>{{ (current_month_group.name | append: "-01") | date: "%B %Y" }}</summary>
  <ul>
  {% for file in current_month_group.items %}
    <li><a href="{{ file.url }}">{{ file.title | date: "%B %d, %Y" }}</a></li>
  {% endfor %}
  </ul>
</details>
{% assign previous_year = current_month_group.name | slice: 0, 4 %}
{% endif %}

{% assign other_months = sorted_groups | where_exp: "month", "month.name != current_month_key" %}
{% for month in other_months %}
  {% assign current_year = month.name | slice: 0, 4 %}
  {% if previous_year and previous_year != current_year %}
<hr>
  {% endif %}
  <details>
    <summary>{{ (month.name | append: "-01") | date: "%B %Y" }}</summary>
    <ul>
    {% for file in month.items %}
      <li><a href="{{ file.url }}">{{ file.title | date: "%B %d, %Y" }}</a></li>
    {% endfor %}
    </ul>
  </details>
  {% assign previous_year = current_year %}
{% endfor %}
