import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# cd /Users/harshithapalia/Desktop/Python/Streamlit/exam_scores

st.set_page_config(page_title="Unit Test 1 Scores 2023-24", layout="wide")

st.title("Unit Test 1 Scores 2023-24")

df = pd.read_csv("ut_1to8_scores_long.csv")
df["Grade"] = df["Grade"].astype(str)
grouped_df_mean = df.groupby(["Grade","Subject"], as_index=False)["Marks"].mean()
grouped_df= df.groupby(["School", "Grade","Section","Subject","Level"], 
                       as_index=False)["Marks"].mean()

st.subheader("Subject Average Across Grades")

subject_list_1 = sorted(df.Subject.unique())
select_subject_1 = st.selectbox("Subject", options = subject_list_1, index = 2)
df_query_1 = grouped_df_mean.query('Subject == @select_subject_1')
query_copy_1 = df_query_1.copy()

fig_1 = px.bar(query_copy_1, x="Grade", y="Marks", title=f"{select_subject_1}", 
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

grouped_df_mean_level = df.groupby(["Grade","Subject","Level"], 
                                   as_index=False)["Marks"].mean()

st.subheader("Subject Average Across Grades - Level Wise")

subject_list_1l = sorted(df.Subject.unique())
select_subject_1l = st.selectbox("Subject", options = subject_list_1l, index = 2,  key = "s1l")
df_query_1l = grouped_df_mean_level.query('Subject == @select_subject_1l')
query_copy_1l = df_query_1l.copy()

fig_1l = px.bar(query_copy_1l, x="Grade", y="Marks", title=f"{select_subject_1l}", 
                text="Marks", color = "Level", barmode = "group",template = "plotly", 
                hover_data={'Marks':':.2f'})
fig_1l.update_layout(title_x=0.5)
fig_1l.update_traces(texttemplate='%{y:.2f}', textfont_size=15)
fig_1l.update_yaxes(range=[0, 100])
fig_1l.update_xaxes(title_text='Grade')
fig_1l.update_yaxes(title_text='Average Score (%)')
fig_1l.add_annotation(text="Average Score Across Grades",
            font=dict(size=16),           
            xref="paper", yref="paper",
            x=0.5, y=1.08, showarrow=False)

st.plotly_chart(fig_1l, use_container_width = True)

grouped_df_mean_level_school = df.groupby(["Grade","Subject","Type","Level"], 
                                   as_index=False)["Marks"].mean()

st.subheader("Subject Average Across Grades - Level Wise - Half/Full Day")

grade_list_ls = sorted(df.Grade.unique())
select_grade_ls = st.selectbox("Grade", options = grade_list_ls, key = "sgls")

subject_list_ls = sorted(df[df["Grade"] == select_grade_ls].Subject.unique())
select_subject_ls = st.selectbox("Subject", options = subject_list_ls, key = "ssls")

df_query_2_ls = grouped_df_mean_level_school.query('Grade == @select_grade_ls and Subject == @select_subject_ls')
query_copy_2_ls = df_query_2_ls.copy()
fig_2ls = px.bar(query_copy_2_ls, x = "Type", y = "Marks", text = "Marks", 
               color = "Level", barmode = "group", template = "plotly", 
               hover_data={'Marks':':.2f'})
fig_2ls.update_layout(xaxis={'categoryorder':'category descending'})
fig_2ls.update_layout(title=f"Grade {select_grade_ls} - {select_subject_ls}", title_x=0.5)
fig_2ls.update_yaxes(range=[0, 100])
fig_2ls.update_xaxes(title_text='Level')
fig_2ls.update_yaxes(title_text='Average Score (%)')
fig_2ls.update_traces(texttemplate='%{y:.2f}')
fig_2ls.update_traces(textposition='inside', textangle=0)

st.plotly_chart(fig_2ls, use_container_width = True)


grouped_df_mean_school = df.groupby(["School","Grade","Subject"], 
                                    as_index=False)["Marks"].mean()

st.subheader("Subject Average Across Grades - School Wise")

subject_list_1s = sorted(df.Subject.unique())
select_subject_1s = st.selectbox("Subject", options = subject_list_1s, key = "s1s")
df_query_1s = grouped_df_mean_school.query('Subject == @select_subject_1s')
query_copy_1s = df_query_1s.copy()

fig_1s = px.bar(query_copy_1s, x="Grade", y="Marks", title=f"{select_subject_1s}", 
                text="Marks", color = "School", barmode = "group",template = "plotly", 
                hover_data={'Marks':':.2f'})
fig_1s.update_layout(title_x=0.5)
fig_1s.update_traces(texttemplate='%{y:.2f}', textfont_size = 15)
fig_1s.update_yaxes(range=[0, 100])
fig_1s.update_xaxes(title_text='Grade')
fig_1s.update_yaxes(title_text='Average Score (%)')
fig_1s.add_annotation(text="Average Score Across Grades",
            font=dict(size=16),           
            xref="paper", yref="paper",
            x=0.5, y=1.08, showarrow=False)

st.plotly_chart(fig_1s, use_container_width = True)


st.subheader("Section Wise Breakdown of Scores")

grade_list = sorted(df.Grade.unique())
select_grade = st.selectbox("Grade", options = grade_list)

subject_list = sorted(df[df["Grade"] == select_grade].Subject.unique())
select_subject = st.selectbox("Subject", options = subject_list)

df_query_2 = grouped_df.query('Grade == @select_grade and Subject == @select_subject')
query_copy_2 = df_query_2.copy()
l0 = df.query('Grade == @select_grade and Subject == @select_subject')["Marks"].mean().round(2)
l1 = grouped_df.query('Grade == @select_grade and Subject == @select_subject and Level == "L1"')["Marks"].mean().round(2)
l2 = grouped_df.query('Grade == @select_grade and Subject == @select_subject and Level == "L2"')["Marks"].mean().round(2)
fig_2 = px.bar(query_copy_2, x = "Section", y = "Marks", text = "Marks", 
               color = "School", pattern_shape = "Level", template = "plotly", 
               hover_data={'Marks':':.2f'})
fig_2.update_layout(xaxis={'categoryorder':'category ascending'})
fig_2.update_layout(title=f"Grade {select_grade} - {select_subject}", title_x=0.5)
fig_2.update_yaxes(range=[0, 100])
fig_2.update_xaxes(title_text='Grade Sections')
fig_2.update_yaxes(title_text='Average Score (%)')
fig_2.update_traces(texttemplate='%{y:.2f}')
fig_2.update_traces(textposition='inside', textangle=0)
fig_2.add_hline(y=l0, line_dash = "dash", line_width = 0.75) 
                #annotation_text=mean_line, 
                #annotation_position="top left")
fig_2.add_annotation(text=f"- - - Grade Average: {l0}",
    xref="paper", yref="paper",
    x=0.05, y=1, showarrow=False, font_size=15)
fig_2.add_annotation(text=f"L2 Average: {l2}",
    xref="paper", yref="paper",
    x=0.5, y=1, showarrow=False, font_size=15)
fig_2.add_annotation(text=f"L1 Average: {l1}",
    xref="paper", yref="paper",
    x=0.9, y=1, showarrow=False, font_size=15)

st.plotly_chart(fig_2, use_container_width = True)

st.subheader("Distribution of Scores")

grade_list_3 = sorted(df.Grade.unique())
select_grade_3 = st.selectbox("Grade", options = grade_list_3, key = "sg3")

subject_list_3 = sorted(df[df["Grade"] == select_grade_3].Subject.unique())
select_subject_3 = st.selectbox("Subject", options = subject_list_3, key = "ss3")

df_query_3 = df.query('Grade == @select_grade_3 and Subject == @select_subject_3')
query_copy_3 = df_query_3.copy()

fig_3 = go.Figure()
fig_3.add_trace(go.Histogram(histfunc="count",x=query_copy_3["Marks"],
                            xbins=dict(start=0,end=100,size=10),
                            texttemplate="%{y}",textangle=0))
fig_3.update_layout(title=f"Grade {select_grade_3} - {select_subject_3}", 
                    title_x=0.5, bargap=0.05)
fig_3.update_xaxes(title_text='Percentage Obtained (%)', range=[0, 100])
fig_3.update_yaxes(title_text='Count of Students')
fig_3.update_layout(xaxis = dict(tickmode = 'linear', tick0 = 0.0, dtick = 10))
fig_3.update_traces(textfont_size=15)

st.plotly_chart(fig_3, use_container_width = True)
