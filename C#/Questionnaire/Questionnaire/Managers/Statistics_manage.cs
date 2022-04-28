using Questionnaire.Helpers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Questionnaire.Managers
{
    public class Statistics_manage
    {
        public List<Question> GetmanageQuestion(int QuestionnaireID, int QType)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT ID, Title,Answer FROM Question
                    WHERE QuestionnaireID = @QuestionnaireID AND QType = @QType
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.Parameters.AddWithValue("@QType", QType);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<Question> questionDatas = new List<Question>();

                        while (reader.Read())
                        {
                            Question questionData = new Question()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                            };
                            questionDatas.Add(questionData);
                        }

                        return questionDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }

        public List<StatisticsData> GetStatistics(int QuestionnaireID, int QType, int QuestionID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT
	                    Answer.QuestionID
	                    ,Question.Title
	                    ,Answer.Answer
	                    ,count(Answer.Answer) AS 'Count'
	                    , QType
	
                    FROM Answer
                    JOIN Question
                    ON Answer.QuestionID = Question.ID
                    WHERE QType =@QType AND Question.QuestionnaireID = @QuestionnaireID  AND QuestionID = @QuestionID
                    GROUP BY Title, Answer.Answer, Answer.QuestionID, QType
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.Parameters.AddWithValue("@QType", QType);
                        command.Parameters.AddWithValue("@QuestionID", QuestionID);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<StatisticsData> StatisticsDatas = new List<StatisticsData>();

                        while (reader.Read())
                        {
                            StatisticsData StatisticsData = new StatisticsData()
                            {
                                QuestionID = (int)reader["QuestionID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                                Count = (int)reader["Count"],
                                QType = (int)reader["QType"],
                            };
                            StatisticsDatas.Add(StatisticsData);
                        }

                        return StatisticsDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }

        public List<StatisticsData> GetStatisticsTwo(int QuestionnaireID, int QType, int QuestionID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT
	                    Answer.QuestionID
	                    ,Question.Title
	                    ,Answer.Answer
	
                    FROM Answer
                    JOIN Question
                    ON Answer.QuestionID = Question.ID
                    WHERE QType = @QType AND Question.QuestionnaireID = @QuestionnaireID AND QuestionID = @QuestionID
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.Parameters.AddWithValue("@QType", QType);
                        command.Parameters.AddWithValue("@QuestionID", QuestionID);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<StatisticsData> StatisticsDatas = new List<StatisticsData>();

                        while (reader.Read())
                        {
                            StatisticsData StatisticsData = new StatisticsData()
                            {
                                QuestionID = (int)reader["QuestionID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                            };
                            StatisticsDatas.Add(StatisticsData);
                        }

                        return StatisticsDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }



    }
}