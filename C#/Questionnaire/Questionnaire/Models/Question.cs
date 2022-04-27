using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Questionnaire.Models
{
    public class Question
    {
        public string joinsessionsID { get; set; }


        public int ID { get; set; }
        public int QuestionnaireID { get; set; }
        public string Title { get; set; }
        public string Answer { get; set; }
        public int QType { get; set; }
        public bool Required { get; set; }


        public int QuestionID { get; set; }


        public string Choose { get; set; }

        

    }
}