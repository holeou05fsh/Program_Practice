using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Questionnaire.Models
{
    public class AnswerData
    {
        //=====================Personalinfo======================

        public Int64 Sort { get; set; }
        public int ID { get; set; }
        public int QuestionnaireID { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
        public int Phone { get; set; }
        public string Email { get; set; }
        public DateTime Date { get; set; }

        //=====================Answer======================


    }
}