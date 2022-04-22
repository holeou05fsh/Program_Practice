﻿using Questionnaire.Helpers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Questionnaire.Managers
{
    public class Questionnaire_manage
    {
        /// <summary> 前台列表分頁 </summary>
        /// <param name="PageSize">頁面顯示量</param>
        /// <param name="PageIndex">頁數</param>
        /// <returns></returns>
        public List<QuestionnaireData> GetFontQuestionnaire(string keyword, string StartTime, string EndTime, int PageSize, int PageIndex, out int totalRows)
        {
            int skip = PageSize * (PageIndex - 1);  //計算跳頁數
            if (skip < 0)
                skip = 0;

            string whereConition = string.Empty;
            if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
                whereConition = @" AND Title LIKE '%'+@Keyword+'%' 
                                   AND StartTime >= @StartTime 
                                   AND EndTime <= @EndTime
                                ";

            string connStr = ConfigString.GetConfigString();
            string commandText =
                $@"
                    SELECT TOP {PageSize} *
                    FROM Questionnaire
                    JOIN 
	                    (
	                    SELECT
		                    ROW_NUMBER() OVER(ORDER BY ID asc)  AS 'Sort'
		                    , ID
	                    FROM Questionnaire
	                    ) AS Temp
                    on Temp.ID = Questionnaire.ID

                    WHERE Questionnaire.State = 1 AND Questionnaire.ID NOT IN 
	                    (
		                    SELECT TOP {skip} ID
		                    FROM Questionnaire
		                    WHERE State = 1
	                              {whereConition}
		                    ORDER BY ID DESC
	                    )
	                    {whereConition}
                    ORDER BY Questionnaire.ID DESC
                ";

            string commandCountText =
            $@"
                SELECT COUNT(ID) AS 'Count'
                FROM Questionnaire
				WHERE State = 1
	            {whereConition}
            ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
                        {
                            command.Parameters.AddWithValue("@keyword", keyword);
                            command.Parameters.AddWithValue("@StartTime", StartTime);
                            command.Parameters.AddWithValue("@EndTime", EndTime);
                        }
                            
                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();

                        List<QuestionnaireData> ChapterDatas = new List<QuestionnaireData>();
                        while (reader.Read())
                        {
                            string timestate = "已完結";
                            if ((DateTime)reader["EndTime"] > DateTime.Now)
                                timestate = "投票中";

                            ChapterDatas.Add(new QuestionnaireData()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Describe = (string)reader["Describe"],
                                StartTime = (DateTime)reader["StartTime"],
                                EndTime = (DateTime)reader["EndTime"], 
                                Timestate = timestate,
                                Sort = (Int64)reader["Sort"]
                            });
                        }
                        reader.Close();

                        //取得總筆數
                        command.CommandText = commandCountText;
                        //C#規定: 每次執行 參數要不同，所以參數查詢要重寫
                        command.Parameters.Clear();
                        if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
                        {
                            command.Parameters.AddWithValue("@keyword", keyword);
                            command.Parameters.AddWithValue("@StartTime", StartTime);
                            command.Parameters.AddWithValue("@EndTime", EndTime);
                        }
                        totalRows = (int)command.ExecuteScalar();

                        return ChapterDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }

        public List<QuestionnaireData> GetBackQuestionnaire(string keyword, string StartTime, string EndTime, int PageSize, int PageIndex, out int totalRows1)
        {
            int skip = PageSize * (PageIndex - 1);  //計算跳頁數
            if (skip < 0)
                skip = 0;

            string whereConition = string.Empty;
            string AND = string.Empty;
            string WHERE = string.Empty;
            if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
            {
                whereConition = @" Title LIKE '%'+@Keyword+'%' 
                                   AND StartTime >= @StartTime 
                                   AND EndTime <= @EndTime
                                ";
                AND = "AND";
                WHERE = "WHERE";
            }
                

            string connStr = ConfigString.GetConfigString();
            string commandText =
                $@"
                SELECT TOP {PageSize} *
                FROM Questionnaire
                JOIN 
	                (
	                SELECT
		                ROW_NUMBER() OVER(ORDER BY ID asc)  AS 'Sort'
		                , ID
	                FROM Questionnaire
	                ) AS Temp
                on Temp.ID = Questionnaire.ID

                WHERE Questionnaire.ID NOT IN 
	                (
		                SELECT TOP {skip} ID
		                FROM Questionnaire
                        {WHERE} {whereConition}
		                ORDER BY ID DESC
	                )
	                {AND} {whereConition}
                ORDER BY Questionnaire.ID DESC
            ";

            string commandCountText =
            $@"
                SELECT COUNT(ID) AS 'Count'
                FROM Questionnaire
	            {WHERE} {whereConition}
            ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
                        {
                            command.Parameters.AddWithValue("@keyword", keyword);
                            command.Parameters.AddWithValue("@StartTime", StartTime);
                            command.Parameters.AddWithValue("@EndTime", EndTime);
                        }

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();

                        List<QuestionnaireData> ChapterDatas = new List<QuestionnaireData>();
                        while (reader.Read())
                        {
                            string strstate = "開啟";
                            if (!(bool)reader["State"])
                                strstate = "已關閉";
                                
                            QuestionnaireData questionnaireData = new QuestionnaireData()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Describe = (string)reader["Describe"],
                                StartTime = (DateTime)reader["StartTime"],
                                EndTime = (DateTime)reader["EndTime"],
                                State = (bool)reader["State"],
                                StrState = strstate,
                            };
                            ChapterDatas.Add(questionnaireData);
                        }
                        reader.Close();
                        //取得總筆數
                        command.CommandText = commandCountText;
                        command.Parameters.Clear();
                        if (!string.IsNullOrEmpty(keyword) && !string.IsNullOrEmpty(StartTime) && !string.IsNullOrEmpty(EndTime))
                        {
                            command.Parameters.AddWithValue("@keyword", keyword);
                            command.Parameters.AddWithValue("@StartTime", StartTime);
                            command.Parameters.AddWithValue("@EndTime", EndTime);
                        }
                        totalRows1 = (int)command.ExecuteScalar();
                        return ChapterDatas;
                    }
                }
            }
            catch
            {
                throw;
            }
        }

        public void delQuestionnaire(string[] IDs)
        {
            List<int> intIDs = IDs
            .Select(s => { int i; return int.TryParse(s, out i) ? i : (int?)null; })
            .Where(i => i.HasValue)
            .Select(i => i.Value)
            .ToList();

            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    DELETE Questionnaire
                                    WHERE ID = @ID
                                ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        foreach (int ID in intIDs)
                        {
                            connection.Open();
                            command.Parameters.AddWithValue("@ID", ID);
                            command.ExecuteNonQuery();
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }

        public QuestionnaireData GetmanageQuestionnaire(int ID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText =
                @"
                    SELECT * FROM Questionnaire
                    WHERE ID = @ID
                ";

            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        command.Parameters.AddWithValue("@ID", ID);

                        connection.Open();
                        SqlDataReader reader = command.ExecuteReader();

                        if (reader.Read())
                        {
                            QuestionnaireData questionnaireData = new QuestionnaireData()
                            {
                                ID = (int)reader["ID"],
                                Title = (string)reader["Title"],
                                Describe = (string)reader["Describe"],
                                StartTime = (DateTime)reader["StartTime"],
                                EndTime = (DateTime)reader["EndTime"],
                                State = (bool)reader["State"],
                            };
                            return questionnaireData;
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

        public void insertQuestionnaire(string Title, string Describe, DateTime StartTime, DateTime EndTime, byte State, out int MaxID)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    INSERT INTO Questionnaire
                                        (Title, Describe, StartTime, EndTime, State)
                                    VALUES
                                        (@Title, @Describe, @StartTime, @EndTime, @State)
                                ";
            string commandMaxIDText =
            $@"
                SELECT MAX(ID) FROM Questionnaire
            ";
            try
            {
                using (SqlConnection connection = new SqlConnection(connStr))
                {
                    using (SqlCommand command = new SqlCommand(commandText, connection))
                    {
                        connection.Open();
                        command.Parameters.AddWithValue("@Title", Title);
                        command.Parameters.AddWithValue("@Describe", Describe);
                        command.Parameters.AddWithValue("@StartTime", StartTime);
                        command.Parameters.AddWithValue("@EndTime", EndTime);
                        command.Parameters.AddWithValue("@State", State);

                        command.ExecuteNonQuery();

                        command.CommandText = commandMaxIDText;
                        MaxID = (int)command.ExecuteScalar();
                    }
                }
            }
            catch (Exception ex)
            {
                throw;
            }
        }

        public void UpdateQuestionnaire(int ID, string Title, string Describe, DateTime StartTime, DateTime EndTime, byte State)
        {
            string connStr = ConfigString.GetConfigString();
            string commandText = @"
                                    UPDATE Questionnaire
                                    SET
                                        Title = @Title, 
                                        Describe = @Describe, 
                                        StartTime = @StartTime, 
                                        EndTime = @EndTime, 
                                        State = @State
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
                        command.Parameters.AddWithValue("@Title", Title);
                        command.Parameters.AddWithValue("@Describe", Describe);
                        command.Parameters.AddWithValue("@StartTime", StartTime);
                        command.Parameters.AddWithValue("@EndTime", EndTime);
                        command.Parameters.AddWithValue("@State", State);
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