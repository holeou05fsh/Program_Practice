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

        public void insertQuestion(int QuestionnaireID, string title, string answer, int qtype, byte required) //, out int newQuestionid
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    INSERT INTO Question
                                        (QuestionnaireID, title, answer, qtype, required)
                                    VALUES
                                        (@QuestionnaireID, @title, @answer, @qtype, @required)
                                ";
            //string commandMaxIDText =
            //$@"
            //    SELECT MAX(ID) FROM Question
            //";
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

                        //command.CommandText = commandMaxIDText;
                        //newQuestionid = (int)command.ExecuteScalar();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }

        public void updateAnswer(int ID, int newQuestionid)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    UPDATE Answer
                                    SET QuestionID = @newQuestionid
                                    WHERE QuestionID = @ID
                                 ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@ID", ID);
                        command.Parameters.AddWithValue("@newQuestionid", newQuestionid);

                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }


        //========================================================

        public void insertPersonalinfo(int QuestionnaireID, string Name, int Age, int Phone, string Email, DateTime Date, out int PersonalinfoID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                   INSERT INTO Personalinfo
                                        (QuestionnaireID, Name, Age, Phone, Email, Date)
                                    VALUES
                                        (@QuestionnaireID, @Name, @Age, @Phone, @Email, @Date)
                                ";
            string commandMaxIDText =
            $@"
                SELECT MAX(ID) FROM Personalinfo
            ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@QuestionnaireID", QuestionnaireID);
                        command.Parameters.AddWithValue("@Name", Name);
                        command.Parameters.AddWithValue("@Age", Age);
                        command.Parameters.AddWithValue("@Phone", Phone);
                        command.Parameters.AddWithValue("@Email", Email);
                        command.Parameters.AddWithValue("@Date", Date);

                        command.ExecuteNonQuery();

                        command.CommandText = commandMaxIDText;
                        PersonalinfoID = (int)command.ExecuteScalar();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }


        public void insertAnswer(int PersonalinfoID, int QuestionID, string Answer, DateTime Date)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                   INSERT INTO Answer
                                        (PersonalinfoID, QuestionID, Answer, Date)
                                    VALUES
                                        (@PersonalinfoID, @QuestionID, @Answer, @Date)
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@PersonalinfoID", PersonalinfoID);
                        command.Parameters.AddWithValue("@QuestionID", QuestionID);
                        command.Parameters.AddWithValue("@Answer", Answer);
                        command.Parameters.AddWithValue("@Date", Date);

                        command.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }



        //===================================================================================

        public List<Question> GetmanageAnswer(int PersonalinfoID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    select 
	                    Answer.QuestionID
	                    ,Answer.Answer
	                    ,Question.QType
                    from Answer

                    join Question
                    on Question.ID = Answer.QuestionID
                    where PersonalinfoID= @PersonalinfoID;
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@PersonalinfoID", PersonalinfoID);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();
                        List<Question> questionDatas = new List<Question>();

                        while (reader.Read())
                        {
                            Question questionData = new Question()
                            {
                                QuestionID = (int)reader["QuestionID"],
                                Answer = (string)reader["Answer"],
                                QType = (int)reader["QType"],
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






    }
}