from jinja2 import Template 

RULE_TEMPLATE = Template("""
<rule id="rule1">
  <name>Sample Rule</name>
  <description>Sample description</description>
  <priority>5</priority>
  <event_threshold value="25" time_span="120" />
  <search>
    <query>sourceIP="1.2.3.4"</query>
  </search>
  <correlation_threshold value="5" time_span="30" />
  <offense_ttl>30</offense_ttl>
  <rebuild_event_threshold>false</rebuild_event_threshold>
  <type>0</type>
  <status>1</status>
  <context>Context</context>
  <cre_user>admin</cre_user>
  <cre_time>1234567890</cre_time>
</rule>
""")

rule = RULE_TEMPLATE.render()

with open('rules/rule1.xml', 'w') as f:
  f.write(rule)