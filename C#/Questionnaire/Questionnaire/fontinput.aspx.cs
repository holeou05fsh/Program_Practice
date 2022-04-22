using Questionnaire.Managers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Questionnaire
{
    public partial class fontinput : System.Web.UI.Page
    {
        private Questionnaire_manage _qtmgr = new Questionnaire_manage();


        protected void Page_Load(object sender, EventArgs e)
        {
            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);
            if (QSID != null && QSID != 0)
            {
                QuestionnaireData FontinputquestionnaireData = _qtmgr.GetfontinputQuestionnaire((int)QSID);
                this.lilTimestate.Text = FontinputquestionnaireData.Timestate;
                this.lilStartTime.Text = Convert.ToDateTime(FontinputquestionnaireData.StartTime.ToString()).ToString("yyyy-MM-dd");
                this.lilEndTime.Text = Convert.ToDateTime(FontinputquestionnaireData.EndTime.ToString()).ToString("yyyy-MM-dd");
                this.lilDescribe.Text = FontinputquestionnaireData.Describe;
                this.lilTitle.Text = FontinputquestionnaireData.Title;
            }
            else
            {
                Response.Redirect("https://c.tenor.com/rkm2Az4596oAAAAM/angry-baby-crypcorp.gif");
            }

        }

        protected void btnCancel_Click(object sender, EventArgs e)
        {
            Response.Redirect("/index.aspx");
        }

        protected void btnSure_Click(object sender, EventArgs e)
        {
            this.PlaceHolder1.Visible = false;
            this.PlaceHolder2.Visible = true;
        }

        protected void btnCancel2_Click(object sender, EventArgs e)
        {
            this.PlaceHolder1.Visible = true;
            this.PlaceHolder2.Visible = false;
        }

        protected void btnSure2_Click(object sender, EventArgs e)
        {
            this.PlaceHolder2.Visible = false;
            this.PlaceHolder3.Visible = true;
        }

        protected void btnSure3_Click(object sender, EventArgs e)
        {
            Response.Redirect("/index.aspx");
        }
    }
}