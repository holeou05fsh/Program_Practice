using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Questionnaire.Models
{
    public class StatisticsData
    {

        public int QuestionID { get; set; }
        public string Title { get; set; }
        public string Answer { get; set; }
        public int Count { get; set; }
        public int QType { get; set; }
        public int PersonalinfoID { get; set; }
        
    }
}