using Questionnaire.Managers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.Web.UI.WebControls;

namespace Questionnaire
{
    public partial class index : System.Web.UI.Page
    {
        private Questionnaire_manage _qtmgr = new Questionnaire_manage();

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                this.txtEndTime.Text = Convert.ToDateTime(DateTime.Now.ToString()).ToString("yyyy-MM-dd");

                this.txtEndTime1.Text = Convert.ToDateTime(DateTime.Now.ToString()).ToString("yyyy-MM-dd");

                int Pagesize = 4;
                int? Pageindex = Convert.ToInt32(Request.QueryString["Page"]);
                if (Pageindex == null || Pageindex <= 1)
                    Pageindex = 1;

                int totalRows = 0;

                string keyword = this.Request.QueryString["keyword"];
                string StartTime = this.Request.QueryString["StartTime"];
                string EndTime = this.Request.QueryString["EndTime"];

                List<QuestionnaireData> FontquestionnaireData = _qtmgr.GetFontQuestionnaire(keyword, StartTime, EndTime, Pagesize, (int)Pageindex, out totalRows);
                this.Repeater1.DataSource = FontquestionnaireData;
                this.Repeater1.DataBind();

                int totalRows1 = 0;
                List<QuestionnaireData> BackquestionnaireData = _qtmgr.GetBackQuestionnaire(keyword, StartTime, EndTime, Pagesize, (int)Pageindex, out totalRows1);
                this.Repeater2.DataSource = BackquestionnaireData;
                this.Repeater2.DataBind();

                string path = Server.HtmlEncode(Request.Path);
                string[] backpath = path.Split('/');
                if (backpath.Length > 2 && backpath[2] == "backindex")
                {
                    this.PlaceHolder1.Visible = false;
                    this.PlaceHolder2.Visible = true;
                    this.lblindextitle.Text = "後台 - 問卷管理";
                }

                NameValueCollection nvcQS = new NameValueCollection();

                if ( keyword != "" && StartTime != "" && EndTime != "")
                {
                    nvcQS.Add("keyword", keyword);
                    nvcQS.Add("StartTime", StartTime);
                    nvcQS.Add("EndTime", EndTime); 
                }
                this.ucPagination.TotalRows = totalRows;
                this.ucPagination.PageIndex = (int)Pageindex;
                this.ucPagination.Bind(nvcQS);
                this.ucPagination1.TotalRows = totalRows1;
                this.ucPagination1.PageIndex = (int)Pageindex;
                this.ucPagination1.Bind(nvcQS);
            }
        }

        protected void btnbackindex_Click(object sender, EventArgs e)
        {
            string path = Server.HtmlEncode(Request.Path);
            string[] backpath = path.Split('/');
            if (backpath.Length > 2 && backpath[2] == "backindex")
            {
                Response.Redirect("/index.aspx");
            }
            else
            {
                Response.Redirect("/index.aspx/backindex");
            }
        }

        protected void btnplus_Click(object sender, EventArgs e)
        {
            Response.Redirect("/endmanage.aspx");
        }

        protected void btndelete_Click(object sender, EventArgs e)
        {
            string[] vals = this.Request.Form.GetValues("backlistcheck");
            _qtmgr.delQuestionnaire(vals);
            Response.Redirect(Request.RawUrl);
        }


        protected void btnSearch_Click(object sender, EventArgs e)
        {
            string keyword = this.txtkeyword.Text;
            string StartTime = this.txtStartTime.Text;
            string EndTime = this.txtEndTime.Text;

            if (keyword != "" && StartTime != "" && EndTime != "")
            {
                string url = this.Request.Url.LocalPath +
                "?keyword=" + keyword +
                "&StartTime=" + StartTime +
                "&EndTime=" + EndTime;

                this.Response.Redirect(url);
            }
            
        }

        protected void btnSearch1_Click(object sender, EventArgs e)
        {
            string keyword = this.txtkeyword1.Text;
            string StartTime = this.txtStartTime1.Text;
            string EndTime = this.txtEndTime1.Text;

            if (keyword != "" && StartTime != "" && EndTime != "")
            {
                string url = this.Request.Url.LocalPath +
                "?keyword=" + keyword +
                "&StartTime=" + StartTime +
                "&EndTime=" + EndTime;

                this.Response.Redirect(url);
            }
        }
    }
}