using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Questionnaire.Models
{
    public class StatisticsData
    {
        //======================SQL==========================
        public int QuestionID { get; set; }
        public string Title { get; set; }
        public string Answer { get; set; }
        public int Count { get; set; }
        public int QType { get; set; }
        public int PersonalinfoID { get; set; }


        //========================Statistic========================
        
        public int S_ID { get; set; }
        public string S_Title { get; set; }
        public string S_Answer { get; set; }
        public string S_Rate { get; set; }
        public string S_Count { get; set; }



    }
}