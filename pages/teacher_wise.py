import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Unit Test 1 Scores 2023-24")

df = pd.read_csv("ut_1to8_scores_long.csv")
df["Grade"] = df["Grade"].astype(str)

grouped_df1= df.groupby(["Grade","Subject","Teacher"], 
                       as_index=False)["Marks"].mean()

grouped_df2= df.groupby(["Grade","Subject","Level","Teacher"], 
                       as_index=False)["Marks"].mean()

grade_list = sorted(df.Grade.unique())
select_grade = st.selectbox("Grade", options = grade_list)

subject_list = sorted(df[df["Grade"] == select_grade].Subject.unique())
select_subject = st.selectbox("Subject", options = subject_list)


st.subheader("Subject Average Across Grades")

df_query_1 = grouped_df1.query('Grade == @select_grade and Subject == @select_subject')
query_copy_1 = df_query_1.copy()

fig_1 = px.bar(query_copy_1, x="Teacher", y="Marks", title=f"Grade {select_grade} - {select_subject}", 
               text="Marks", template = "plotly", hover_data={'Marks':':.2f'})
fig_1.update_layout(title_x=0.5)
fig_1.update_traces(texttemplate='%{y:.2f}', textfont_size=20)
fig_1.update_yaxes(range=[0, 100])
fig_1.update_xaxes(title_text='Grade')
fig_1.update_yaxes(title_text='Average Score (%)')
fig_1.add_annotation(text="Average Score Across Grades",
            font=dict(size=16),           
            xref="paper", yref="paper",
            x=0.5, y=1.08, showarrow=False)

st.plotly_chart(fig_1, use_container_width = True)

st.subheader("Subject Average Across Grades - Level Wise")

df_query_2 = grouped_df2.query('Grade == @select_grade and Subject == @select_subject')
query_copy_2 = df_query_2.copy()

fig_2 = px.bar(query_copy_2, x="Teacher", y="Marks", title=f"Grade {select_grade} - {select_subject}", 
               text="Marks", color = "Level", barmode = "group", 
               template = "plotly", hover_data={'Marks':':.2f'})
fig_2.update_layout(title_x=0.5)
fig_2.update_traces(texttemplate='%{y:.2f}', textfont_size=20)
fig_2.update_yaxes(range=[0, 100])
fig_2.update_xaxes(title_text='Grade')
fig_2.update_yaxes(title_text='Average Score (%)')
fig_2.add_annotation(text="Average Score Across Grades",
            font=dict(size=16),           
            xref="paper", yref="paper",
            x=0.5, y=1.08, showarrow=False)

st.plotly_chart(fig_2, use_container_width = True)

st.subheader("Subject Average Across Grades - Teacher Wise")

grouped_df3= df.groupby(["Grade","Section","Level","Subject","Teacher"], 
                       as_index=False)["Marks"].mean()

df_query_3 = grouped_df3.query('Grade == @select_grade and Subject == @select_subject')
query_copy_3 = df_query_3.copy()

fig_3 = px.bar(query_copy_3, x="Section", y="Marks", 
               title=f"Grade {select_grade} - {select_subject}", 
               text="Marks", color = "Level", 
               facet_col = "Teacher", facet_col_wrap = 2, 
               facet_col_spacing = 0.1, facet_row_spacing = 0.15,
               template = "plotly", hover_data={'Marks':':.2f'},
               height = 1200)
fig_3.update_layout(title_x=0.5)
fig_3.update_traces(texttemplate='%{y:.2f}', textfont_size=20)
fig_3.update_yaxes(range=[0, 100])
fig_3.update_xaxes(title_text='Grade')
fig_3.update_yaxes(title_text='Average Score (%)')
fig_3.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig_3.update_annotations(font = dict(size=22))
# fig_3.add_annotation(text="Average Score Across Grades",
#             font=dict(size=16),           
#             xref="paper", yref="paper",
#             x=0.5, y=1.08, showarrow=False)
fig_3.update_xaxes(matches=None)
fig_3.for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))

st.plotly_chart(fig_3, use_container_width = True)