using Questionnaire.Helpers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Questionnaire.Managers
{
    public class Question_manage
    {
        public List<Question> GetmanageQuestion(int QuestionnaireID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT * FROM Question
                    WHERE QuestionnaireID = @QuestionnaireID
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<Question> questionDatas = new List<Question>();

                        while (reader.Read())
                        {
                            Question questionData = new Question()
                            {
                                ID = (int)reader["ID"],
                                QuestionnaireID = (int)reader["QuestionnaireID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                                QType = (int)reader["QType"],
                                Required = (bool)reader["Required"],
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

        public void delQuestion(int QuestionnaireID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    DELETE Question
                                    WHERE QuestionnaireID = @QuestionnaireID
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }

        public void insertQuestion(int QuestionnaireID, string title, string answer, int qtype, byte required)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    INSERT INTO Question
                                        (QuestionnaireID, title, answer, qtype, required)
                                    VALUES
                                        (@QuestionnaireID, @title, @answer, @qtype, @required)
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.Parameters.AddWithValue("@title", title);
                        command.Parameters.AddWithValue("@answer", answer);
                        command.Parameters.AddWithValue("@qtype", qtype);
                        command.Parameters.AddWithValue("@required", required);

                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }

        public void updateQuestion(int ID, string answer)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    UPDATE Question
                                    SET
                                        answer = @answer
                                    WHERE ID = @ID
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@ID", ID);
                        command.Parameters.AddWithValue("@answer", answer);

                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }


    }
}