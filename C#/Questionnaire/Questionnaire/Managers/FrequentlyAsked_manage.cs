using Questionnaire.Helpers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Questionnaire.Managers
{

    public class FrequentlyAsked_manage
    {
        public List<Question> GetmanageFrequentlyAsked()
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT * FROM FrequentlyAsked
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<Question> FrequentlyAskedDatas = new List<Question>();

                        while (reader.Read())
                        {
                            Question FrequentlyAskedData = new Question()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                                QType = (int)reader["QType"],
                                Required = (bool)reader["Required"]
                            };
                            FrequentlyAskedDatas.Add(FrequentlyAskedData);
                        }

                        return FrequentlyAskedDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }

        public Question GetmanageFrequentlyAskedOne(int ID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT * FROM FrequentlyAsked
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
                        SqlDataReader reader = command.ExecuteReader();

                        if (reader.Read())
                        {
                            Question FrequentlyAskedData = new Question()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Answer = (string)reader["Answer"],
                                QType = (int)reader["QType"],
                                Required = (bool)reader["Required"]
                            };
                            return FrequentlyAskedData;
                        }
                        return null;
                    }
                }
            }
            catch
            {
                throw;
            }
        }


        public void delQuestion(int ID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    DELETE FrequentlyAsked
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
                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }


        public void insertQuestion(string title, string answer, int qtype, byte required)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    INSERT INTO FrequentlyAsked
                                        (title, answer, qtype, required)
                                    VALUES
                                        (@title, @answer, @qtype, @required)
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
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

    }



}