using Questionnaire.Managers;
using Questionnaire.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Questionnaire
{
    public partial class fontinput : System.Web.UI.Page
    {
        private Questionnaire_manage _qtmgr = new Questionnaire_manage();
        private Question_manage _qmgr = new Question_manage();
        private Statistics_manage _Smgr = new Statistics_manage();

        protected void Page_init(object sender, EventArgs e)
        {

            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);
            if (QSID == null || QSID == 0)
            {
                Response.Redirect("https://c.tenor.com/rkm2Az4596oAAAAM/angry-baby-crypcorp.gif");
            }

            List<Question> questions = _qmgr.GetmanageQuestion((int)QSID);
            if (Request.QueryString["page"] == null)
            {
                QuestionnaireMarker(questions, 0);

            }
            else if (Request.QueryString["page"] == "2")
            {
                QuestionnaireMarker(questions, 1);

                this.PlaceHolder1.Visible = false;
                this.PlaceHolder2.Visible = true;
            }
            else if (Request.QueryString["page"] == "3")
            {
                List<Question> QuestionData = _Smgr.GetmanageQuestion((int)QSID, 1);
                List<StatisticsData> StatisticsDatas = _Smgr.GetStatistics((int)QSID, 1);
                this.Literal5.Text = QuestionData[1].Title;
                string[] answerlist = QuestionData[1].Answer.Split(';');  //  12~15;16~18;19~22;23~30;30~40


                Dictionary<string, string> dic = new Dictionary<string, string>();

                int totalcount = 0;
                foreach (StatisticsData StatisticsData in StatisticsDatas)
                {
                    if (StatisticsData.Answer == "年齡")
                    {
                        dic.Add(StatisticsData.Answer, StatisticsData.Count.ToString()); //19~22:1
                        totalcount += StatisticsData.Count;
                    }
                }


                foreach (string answer in answerlist) //  12~15;16~18;19~22;23~30;30~40
                {
                    if (dic.ContainsKey(answer))  //19~22:1
                    {
                        string ratio = ((100 / totalcount) * Convert.ToInt32(dic[answer])).ToString() + "%";
                        dic[answer] = ratio;
                    }
                    else
                    {
                        dic.Add(answer, "0%");
                    }
                }
                //做2次repleater
                //1次
                //年齡
                
                //2次
                //12~15, 0 %
                //16~18, 0 %
                //19~22, 33 %
                //23~30, 66 %
                //30~40, 0 %

                this.PlaceHolder1.Visible = false;
                this.PlaceHolder2.Visible = false;
                this.PlaceHolder3.Visible = true;
            }


        }

        private void QuestionnaireMarker(List<Question> questions, int writedPage)
        {
            bool writed = false; //判斷有沒有填寫過
            int count = 1;
            foreach (Question question in questions)
            {
                string num = count + ". ";
                int ID = question.ID;
                string title = question.Title;
                string answertotal = question.Answer;
                int QType = question.QType;
                bool Required = question.Required;

                if (Required)
                    num = "*" + count + ". ";

                //判斷Session有值就代表已經寫過
                string QTypecontrol = question.QType == 1 ? "rdo" : question.QType == 2 ? "cbl" : "txt";
                string QTypeID = QTypecontrol + question.ID;
                if (this.Session[QTypeID] != null)
                {
                    writed = true;
                    break;
                }
                else  //未填寫過了
                {
                    if (QType == 1)
                        RadioButtonListcreate(num, ID, title, answertotal, writedPage);
                    else if (QType == 2)
                        CheckBoxListcreate(num, ID, title, answertotal, writedPage);
                    else
                        TextBoxcreate(num, ID, title, writedPage);
                    count += 1;
                }
            }

            //已經填寫過了
            if (writed)
            {
                string[] info = this.Session["info"].ToString().Split(',');

                this.TextBox1.Text = info[0];
                this.TextBox2.Text = info[1];
                this.TextBox3.Text = info[2];
                this.TextBox4.Text = info[3];
                
                this.Literal1.Text = info[0];
                this.Literal2.Text = info[1];
                this.Literal3.Text = info[2];
                this.Literal4.Text = info[3];

                foreach (Question question in questions)
                {
                    string num = count + ". ";
                    int ID = question.ID;
                    string title = question.Title;
                    string answertotal = question.Answer;
                    int QType = question.QType;
                    bool Required = question.Required;

                    if (Required)
                        num = "*" + count + ". ";

                    string QTypecontrol = question.QType == 1 ? "rdo" : question.QType == 2 ? "cbl" : "txt";
                    string QTypeID = QTypecontrol + question.ID;

                    string writedQusetionnaire = this.Session[QTypeID].ToString();


                    if (writedQusetionnaire == "NO")
                    {
                        if (QType == 1)
                            RadioButtonListcreate(num, ID, title, answertotal, writedPage);
                        else if (QType == 2)
                            CheckBoxListcreate(num, ID, title, answertotal, writedPage);
                        else
                            TextBoxcreate(num, ID, title, writedPage);
                        count += 1;
                    }
                    else
                    {
                        if (QType == 1)
                            RadioButtonListwrited(num, ID, title, answertotal, writedQusetionnaire, writedPage);
                        else if (QType == 2)
                            CheckBoxListwrited(num, ID, title, answertotal, writedQusetionnaire, writedPage);
                        else
                            TextBoxwrited(num, ID, title, writedQusetionnaire, writedPage);
                        count += 1;
                    }

                }
            }

            this.litqustioncount.Text = $"共{count - 1}個問題";
        }

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


        }

        protected void btnCancel_Click(object sender, EventArgs e)
        {
            Response.Redirect("/index.aspx");
        }

        protected void btnSure_Click(object sender, EventArgs e)
        {
            bool infocheck = true;
            bool inputcheck = false;

            string name = this.TextBox1.Text.Trim();
            string phone = this.TextBox2.Text.Trim();
            string email = this.TextBox3.Text.Trim();
            string age = this.TextBox4.Text.Trim();

            if (name == "" || phone == "" || email == "" || age == "")
                infocheck = false;
            else
                this.Session["info"] = name + "," + phone + "," + email + "," + age;

            if (infocheck)
            {
                int QSID = Convert.ToInt32(Request.QueryString["ID"]);
                List<Question> questions = _qmgr.GetmanageQuestion(QSID);
                foreach (Question question in questions)
                {
                    string QTypecontrol = question.QType == 1 ? "rdo" : question.QType == 2 ? "cbl" : "txt";
                    string QTypeID = QTypecontrol + question.ID;

                    if (QTypecontrol == "rdo")
                    {
                        RadioButtonList rdovalue = this.Page.FindControl(QTypeID) as RadioButtonList;
                        string rdoanswer = rdovalue.SelectedValue;

                        if (question.Required)
                        {
                            if (rdoanswer == "")
                            {
                                inputcheck = true;
                                break;
                            }
                        }

                        if (rdoanswer == "")
                            this.Session[QTypeID] = "NO";
                        else
                            this.Session[QTypeID] = rdoanswer;
                    }
                    else if (QTypecontrol == "cbl")
                    {
                        List<string> cblanswerlist = new List<string>();
                        CheckBoxList cblvalue = this.Page.FindControl(QTypeID) as CheckBoxList;

                        for (int i = 0; i < cblvalue.Items.Count; i++)
                        {
                            if (cblvalue.Items[i].Selected)
                            {
                                cblanswerlist.Add(cblvalue.Items[i].Value.Trim());
                            }
                        }
                        string cblanswer = string.Join(",", cblanswerlist);
                        if (question.Required)
                        {
                            if (cblanswer == "")
                            {
                                inputcheck = true;
                                break;
                            }
                        }
                        if (cblanswer == "")
                            this.Session[QTypeID] = "NO";
                        else
                            this.Session[QTypeID] = cblanswer;
                    }
                    else if (QTypecontrol == "txt")
                    {
                        TextBox cblvalue = this.Page.FindControl(QTypeID) as TextBox;
                        string txtanswer = cblvalue.Text;
                        if (question.Required)
                        {
                            if (txtanswer == "")
                            {
                                inputcheck = true;
                                break;
                            }
                        }

                        if (txtanswer == "")
                            this.Session[QTypeID] = "NO";
                        else
                            this.Session[QTypeID] = txtanswer;
                    }
                }
            }

            if (!infocheck)
                this.litmsg.Text = "※ 有資訊欄位未填，請再次確認";
            else if (inputcheck)
                this.litmsg.Text = "※ 有必填欄位未填，請再次確認";
            else
                Response.Redirect(Request.RawUrl + "&page=2");

        }

        protected void btnCancel2_Click(object sender, EventArgs e)
        {
            string qsID = Request.QueryString["ID"];
            Response.Redirect("/fontinput.aspx?ID=" + qsID);
        }

        protected void btnSure2_Click(object sender, EventArgs e)
        {
            int PersonalinfoID = 0;

            int QSID = Convert.ToInt32(Request.QueryString["ID"]);
            List<Question> questions = _qmgr.GetmanageQuestion(QSID);
            foreach (Question question in questions)
            {
                int QuestionID = question.ID;
                string QTypecontrol = question.QType == 1 ? "rdo" : question.QType == 2 ? "cbl" : "txt";
                string QTypeID = QTypecontrol + QuestionID;

                string updatedata = this.Session[QTypeID].ToString();
                if (updatedata != "NO")
                {
                    int QuestionnaireID = Convert.ToInt32(Request.QueryString["ID"]);
                    string[] info = this.Session["info"].ToString().Split(',');

                    string Name = info[0];
                    int Phone = Convert.ToInt32(info[1]);
                    string Email = info[2];
                    int Age = Convert.ToInt32(info[3]);
                    DateTime Date = Convert.ToDateTime(DateTime.Now.ToString());
                    if (PersonalinfoID == 0)
                        _qmgr.insertPersonalinfo(QuestionnaireID, Name, Age, Phone, Email, Date, out PersonalinfoID);

                    _qmgr.insertAnswer(PersonalinfoID, QuestionID, updatedata, Date);
                }
            }

            string qsID = Request.QueryString["ID"];
            Response.Redirect("/fontinput.aspx?ID=" + qsID + "&page=3");
        }

        protected void btnSure3_Click(object sender, EventArgs e)
        {
            Response.Redirect("/index.aspx");
        }


        private void RadioButtonListcreate(string num, int ID, string title, string answertotal, int writedPage)
        {
            Label lbl = new Label();
            lbl.Text = "<p>" + num + title + "</p>";
            lbl.ID = "msg" + ID;
            lbl.CssClass = "input-title";
            this.form1.Controls.Add(lbl);

            string[] answers = answertotal.Split(';');
            RadioButtonList rdolist = new RadioButtonList();
            rdolist.ID = "rdo" + ID;
            rdolist.CssClass = "input-radioo";

            for (int j = 0; j < answers.Length; j++)
            {
                ListItem item = new ListItem();
                item.Text = answers[j];
                if (writedPage == 1)
                    item.Attributes["onclick"] = "return false";
                rdolist.Items.Add(item);
            }

            this.form1.Controls.Add(rdolist);
        }
        private void RadioButtonListwrited(string num, int ID, string title, string answertotal, string writedQusetionnaire, int writedPage)
        {
            Label lbl = new Label();
            lbl.Text = "<p>" + num + title + "</p>";
            lbl.ID = "msg" + ID;
            lbl.CssClass = "input-title";
            this.form1.Controls.Add(lbl);

            string[] checkeditem = writedQusetionnaire.Split(',');
            string[] answers = answertotal.Split(';');
            RadioButtonList rdolist = new RadioButtonList();
            rdolist.ID = "rdo" + ID;
            rdolist.CssClass = "input-radioo";

            for (int j = 0; j < answers.Length; j++)
            {
                ListItem item = new ListItem();
                item.Text = answers[j].Trim();

                if (checkeditem.Contains(answers[j]))
                    item.Selected = true;
                if (writedPage == 1)
                    item.Attributes["onclick"] = "return false";
                rdolist.Items.Add(item);
            }

            this.form1.Controls.Add(rdolist);
        }


        private void CheckBoxListcreate(string num, int ID, string title, string answertotal, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "</p>";
            lit.CssClass = "input-title";
            Page.Form.Controls.Add(lit);

            string[] answers = answertotal.Split(';');
            CheckBoxList cblist = new CheckBoxList();
            cblist.ID = "cbl" + ID;
            cblist.CssClass = "input-radioo";
            

            for (int j = 0; j < answers.Length; j++)
            {
                ListItem item = new ListItem();
                item.Text = answers[j];
                if (writedPage == 1)
                    item.Attributes["onclick"] = "return false";
                cblist.Items.Add(item);
            }

            this.form1.Controls.Add(cblist);
        }
        private void CheckBoxListwrited(string num, int ID, string title, string answertotal, string writedQusetionnaire, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "</p>";
            lit.CssClass = "input-title";
            Page.Form.Controls.Add(lit);

            string[] answers = answertotal.Split(';');
            CheckBoxList cblist = new CheckBoxList();
            cblist.ID = "cbl" + ID;
            cblist.CssClass = "input-radioo";

            string[] checkeditem = writedQusetionnaire.Split(',');

            for (int j = 0; j < answers.Length; j++)
            {
                ListItem item = new ListItem();
                item.Text = answers[j];

                if (checkeditem.Contains(answers[j].Trim()))
                    item.Selected = true;
                if (writedPage == 1)
                    item.Attributes["onclick"] = "return false";

                cblist.Items.Add(item);
            }

            this.form1.Controls.Add(cblist);
        }


        private void TextBoxcreate(string num, int ID, string title, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "<p>";
            lit.CssClass = "input-title";
            Page.Form.Controls.Add(lit);

            TextBox txt = new TextBox();
            txt.ID = "txt" + ID;
            txt.CssClass = "input-txtinput";
            if (writedPage == 1)
                txt.ReadOnly = true;
            this.form1.Controls.Add(txt);
        }
        private void TextBoxwrited(string num, int ID, string title, string writedQusetionnaire, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "<p>";
            lit.CssClass = "input-title";
            Page.Form.Controls.Add(lit);

            TextBox txt = new TextBox();
            txt.ID = "txt" + ID;
            txt.CssClass = "input-txtinput";
            txt.Text = writedQusetionnaire;

            if (writedPage==1)
                txt.ReadOnly = true;

            this.form1.Controls.Add(txt);
        }

    }
}