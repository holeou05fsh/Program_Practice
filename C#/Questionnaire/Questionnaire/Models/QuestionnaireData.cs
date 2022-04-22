using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Questionnaire.Models
{
    public class QuestionnaireData
    {
        public int ID { get; set; }
        public string Title { get; set; }
        public string Describe { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }
        public string Timestate { get; set; }
        public bool State { get; set; }
        public Int64 Sort { get; set; }
        public string StrState { get; set; }
        
    }
}