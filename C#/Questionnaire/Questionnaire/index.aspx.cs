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
        private Question_manage _qmgr = new Question_manage();
        private FrequentlyAsked_manage _famgr = new FrequentlyAsked_manage();


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
                else if (backpath.Length > 2 && backpath[2] == "frequentlyasked")
                {
                    this.PlaceHolder1.Visible = false;
                    this.PlaceHolder2.Visible = true;
                    this.PlaceHolder3.Visible = false;
                    this.PlaceHolder4.Visible = true;
                    this.lblindextitle.Text = "後台 - 常用問題管理";
                }

                NameValueCollection nvcQS = new NameValueCollection();

                if (keyword != "" && StartTime != "" && EndTime != "")
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


                List<Question> FrequentlyAsked = _famgr.GetmanageFrequentlyAsked();
                this.Repeater3.DataSource = FrequentlyAsked;
                this.Repeater3.DataBind();

                if (this.Session["questionedit"] != null)
                {
                    string[] Frequentlyvals = this.Session["questionedit"].ToString().Split(',');
                    this.TextBox5.Text = Frequentlyvals[1];
                    this.TextBox7.Text = Frequentlyvals[2];
                    if (Frequentlyvals[3] == "1")
                        this.DropDownList2.SelectedValue = "單選方塊";
                    else if (Frequentlyvals[3] == "2")
                        this.DropDownList2.SelectedValue = "複選方塊";
                    else
                        this.DropDownList2.SelectedValue = "文字";
                    if (Frequentlyvals[4] == "True")
                        this.CheckBox1.Checked = true;

                    this.Session["questionedit"] = null;
                }

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

        protected void Repeater3_ItemCommand(object source, RepeaterCommandEventArgs e)
        {
            if (e.CommandName == "questionedit")
            {
                string[] Frequentlyvals = e.CommandArgument.ToString().Split(',');
                int ID = Convert.ToInt32(Frequentlyvals[0]);

                this.Session["questionedit"] = e.CommandArgument.ToString();

                _famgr.delQuestion(ID);

                Response.Redirect(Request.RawUrl);

            }
        }


        protected void btndelete1_Click(object sender, EventArgs e)
        {
            string[] strvals = this.Request.Form.GetValues("questionlistcheck");
            int[] intvals = Array.ConvertAll(strvals, s => int.Parse(s));

            if (intvals != null)
            {
                foreach (int val in intvals)
                {
                    _famgr.delQuestion(val);
                }
            }

            Response.Redirect(Request.RawUrl);
        }

        protected void btnjoin_Click(object sender, EventArgs e)
        {
            string title = this.TextBox5.Text.Trim();
            string answer = this.TextBox7.Text.Trim();
            string qtypeSelected = this.DropDownList2.SelectedValue;
            string requiredChecked = this.CheckBox1.Checked.ToString();
            int qtype = 3;
            if (qtypeSelected == "單選方塊")
                qtype = 1;
            else if (qtypeSelected == "複選方塊")
                qtype = 2;
            byte required = 0;
            if (requiredChecked == "True")
                required = 1;

            if (title != "" && answer != "")
            {
                _famgr.insertQuestion(title, answer, qtype, required);
                Response.Redirect(Request.RawUrl);
            }
        }
    }
}