using Questionnaire.Managers;
using Questionnaire.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Questionnaire
{
    public partial class endmanage : System.Web.UI.Page
    {
        private Question_manage _qmgr = new Question_manage();
        private Questionnaire_manage _qtmgr = new Questionnaire_manage();
        private Statistics_manage _Smgr = new Statistics_manage();
        private FrequentlyAsked_manage _famgr = new FrequentlyAsked_manage();

        int Questionnum = 0;
        int QuestionnumTwo = 0;

        private string[] _joinsessions = new string[] {
            "joinsession1", "joinsession2", "joinsession3", "joinsession4",
            "joinsession5", "joinsession6", "joinsession7", "joinsession8",
            "joinsession9", "joinsession10", "joinsession11", "joinsession12",
        };

        protected void Page_Init(object sender, EventArgs e)
        {
            //=========================== Tag-3 ===============================
            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);

            if (QSID != null && QSID != 0)
            {
                if (Convert.ToInt32(Session["questionshow"]) != 1)
                {
                    int Pagetotal = 0;
                    int PageSize = 4;
                    int? Pageindex = Convert.ToInt32(Request.QueryString["Page"]);
                    if (Pageindex == null || Pageindex <= 1)
                        Pageindex = 1;
                    List<AnswerData> BackAnswer = _qtmgr.GetBackPersonalinfos((int)QSID, PageSize, (int)Pageindex, out Pagetotal);
                    this.Repeater2.DataSource = BackAnswer;
                    this.Repeater2.DataBind();

                    string atagurl = Request.RawUrl;

                    for (int i = 0; i < Pagetotal; i++)
                    {
                        if (atagurl.Contains($"&Page={i}"))
                            atagurl = Request.RawUrl.Replace($"&Page={i}", "");
                    }


                    this.ucPagination.Url = atagurl;
                    this.ucPagination.UrlID = "#tab-3";
                    this.ucPagination.TotalRows = Pagetotal;
                    this.ucPagination.PageIndex = (int)Pageindex;
                    this.ucPagination.Bind();

                    this.PlaceHolder1.Visible = true;
                    this.PlaceHolder2.Visible = false;
                }
                else
                {

                    int answerID = Convert.ToInt32(this.Session["btnAnswer"]);

                    AnswerData BackAnswer = _qtmgr.GetBackPersonalinfo(answerID);

                    this.TextBox6.Text = BackAnswer.Name;
                    this.TextBox8.Text = BackAnswer.Phone.ToString();
                    this.TextBox9.Text = BackAnswer.Email;
                    this.TextBox10.Text = BackAnswer.Age.ToString();
                    this.Literal1.Text = "填寫時間  " + BackAnswer.Date.ToString();

                    List<Question> questions = _qmgr.GetmanageQuestion((int)QSID);
                    List<Question> questionsanswer = _qmgr.GetmanageAnswer(answerID);

                    //判斷Session有值就代表已經寫過
                    foreach (Question question in questionsanswer)
                    {
                        string QTypecontrol = question.QType == 1 ? "rdo" : question.QType == 2 ? "cbl" : "txt";
                        string QTypeID = QTypecontrol + question.QuestionID;
                        this.Session[QTypeID] = question.Answer;
                    }


                    QuestionnaireMarker(questions, 1);

                    this.PlaceHolder1.Visible = false;
                    this.PlaceHolder2.Visible = true;
                }
            }

            if (this.Session["tag3"] != null)
            {
                string tag3msg = this.Session["tag3"].ToString();
                this.Literal2.Text = tag3msg;
                this.Session["tag3"] = null;
            }

        }


        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                //=========================== Tag-1 ===============================

                int? QSID = Convert.ToInt32(Request.QueryString["ID"]);
                if (QSID != null && QSID != 0)
                {
                    QuestionnaireData questionnaireData = _qtmgr.GetmanageQuestionnaire((int)QSID);
                    if (questionnaireData != null)
                    {
                        this.TextBox1.Text = questionnaireData.Title;
                        this.TextBox2.Text = questionnaireData.Describe;
                        this.TextBox3.Text = Convert.ToDateTime(questionnaireData.StartTime.ToString()).ToString("yyyy-MM-dd");
                        this.TextBox4.Text = Convert.ToDateTime(questionnaireData.EndTime.ToString()).ToString("yyyy-MM-dd");
                        this.chkopen.Checked = questionnaireData.State;
                    }
                    else
                        Response.Redirect("https://c.tenor.com/rkm2Az4596oAAAAM/angry-baby-crypcorp.gif");
                }
                else
                    this.TextBox3.Text = Convert.ToDateTime(DateTime.Now.ToString()).ToString("yyyy-MM-dd");

                //=========================== Tag-2 ===============================
                //紀錄:
                //方法一:先把SQL抓出來再跟現有的session結合，如果要存SQL就把他全刪掉再重新加入
                //方法二:按加入後 再排序orcheckbox數字中加入"新"字做insert判斷

                //儲存訊息，因為重導向後litmsgSureT就重製了
                if (this.Session["litmsgSureT"] != null)
                {
                    this.litmsgSureT.Text = this.Session["litmsgSureT"].ToString();
                    this.Session["litmsgSureT"] = null;
                }

                //如果是按編輯後，如果是新增的Session就刪掉Session，如果是SQL的就把TheMarkIsisNew改0
                if (Session["editsession"] != null)
                {
                    string editID = this.Session["editsession"].ToString();
                    string[] sessiondata = editID.ToString().Split();

                    if (_joinsessions.Contains(editID))
                        sessiondata = this.Session[editID].ToString().Split();


                    if (sessiondata.Last() != "1")
                    {
                        this.TextBox5.Text = sessiondata[2];
                        this.TextBox7.Text = sessiondata[3];
                        if (sessiondata[4] == "1")
                            this.DropDownList2.SelectedValue = "單選方塊";
                        else if (sessiondata[4] == "2")
                            this.DropDownList2.SelectedValue = "複選方塊";
                        else
                            this.DropDownList2.SelectedValue = "文字";
                        if (sessiondata[5] == "True")
                            this.CheckBox1.Checked = true;

                        Session[editID] = null;
                        Session["editsession"] = null;
                    }
                    else
                    {
                        this.TextBox5.Text = sessiondata[2];
                        this.TextBox7.Text = sessiondata[3];
                        if (sessiondata[4] == "1")
                            this.DropDownList2.SelectedValue = "單選方塊";
                        else if (sessiondata[4] == "2")
                            this.DropDownList2.SelectedValue = "複選方塊";
                        else
                            this.DropDownList2.SelectedValue = "文字";
                        if (sessiondata[5] == "True")
                            this.CheckBox1.Checked = true;

                        sessiondata[6] = "0";
                        this.Session[editID] = String.Join(" ", sessiondata);

                        this.Session["editsession"] = null;
                    }

                }


                List<Question> FrequentlyAskeds = _famgr.GetmanageFrequentlyAsked();

                foreach (Question Asked in FrequentlyAskeds)
                {
                    DropDownList1.Items.Add(new ListItem(Asked.Title, Asked.ID.ToString()));
                }




                //SQL抓的question
                List<Question> sqlquestions = new List<Question>();
                List<Question> Questions = new List<Question>();
                int? QSID_2 = Convert.ToInt32(Request.QueryString["ID"]);

                if (QSID_2 != null && QSID_2 != 0)//假如有ID就true
                {

                    //比對Session裡有沒有資料庫資料了(找到一筆就代表有了)
                    sqlquestions = _qmgr.GetmanageQuestion((int)QSID_2);
                    if (this.Session[_joinsessions[0]] == null)
                    {
                        for (int i = 0; i < sqlquestions.Count; i++)
                        {
                            List<string> sessionquestion = new List<string>();
                            Question data = sqlquestions[i];
                            sessionquestion.Add(data.ID.ToString());
                            sessionquestion.Add(data.QuestionnaireID.ToString());
                            sessionquestion.Add(data.Title.ToString());
                            sessionquestion.Add(data.Answer.ToString());
                            sessionquestion.Add(data.QType.ToString());
                            sessionquestion.Add(data.Required.ToString());
                            sessionquestion.Add("1");

                            string SQLinSession = String.Join(" ", sessionquestion);
                            this.Session[_joinsessions[i]] = SQLinSession;
                        }
                    }


                    // 總Session(SQL跟新加入的Session)放入questionDate中要做資料細節的
                    for (int i = 0; i < _joinsessions.Length; i++)
                    {
                        if (this.Session[_joinsessions[i]] != null)
                        {
                            string[] splitjoinsession = this.Session[_joinsessions[i]].ToString().Split(' ');
                            if (splitjoinsession.Last() != "0")
                            {
                                Question question = new Question()
                                {
                                    //joinsessionsID = _joinsessions[i],
                                    ID = Convert.ToInt32(splitjoinsession[0]),
                                    QuestionnaireID = Convert.ToInt32(splitjoinsession[1]),
                                    Title = splitjoinsession[2],
                                    Answer = splitjoinsession[3],
                                    QType = Convert.ToInt32(splitjoinsession[4]),
                                    Required = splitjoinsession[5] == "1" ? true : false,
                                };
                                Questions.Add(question);
                            }
                        }
                    }

                    this.Repeater1.DataSource = Questions;
                    this.Repeater1.DataBind();

                }

                //=========================== Tag-4 ===============================
                List<Question> QuestionData = _Smgr.GetmanageQuestion((int)QSID, 1);
                List<Question> QuestionData2 = _Smgr.GetmanageQuestion((int)QSID, 2);

                this.Repeater3.DataSource = QuestionData;
                this.Repeater3.DataBind();

                this.Repeater5.DataSource = QuestionData2;
                this.Repeater5.DataBind();
            }
        }


        protected void btnCancel3_Click(object sender, EventArgs e)
        {
            //btnCancel3 session應該是要全刪但有點懶惰，以後要在再說吧
            Session.Abandon();
            this.Session["questionshow"] = 0;
            this.Session["btnAnswer"] = null;

            Response.Redirect(Request.RawUrl + "#tab-3");
        }



        protected void btnCancel_Click(object sender, EventArgs e)
        {
            Response.Redirect("/index.aspx/backindex");
        }

        protected void btnSure_Click(object sender, EventArgs e)
        {

            List<ArrayList> surecheck = SureCheck(1);

            if (surecheck.Count > 0)
            {
                int? QSID = Convert.ToInt32(Request.QueryString["ID"]);
                if (QSID == null || QSID == 0)
                {
                    int MaxID = 0;
                    _qtmgr.insertQuestionnaire((string)surecheck[0][0], (string)surecheck[0][1], Convert.ToDateTime(surecheck[0][2]), Convert.ToDateTime(surecheck[0][3]), (byte)surecheck[0][4], out MaxID);
                    this.TextBox4.Text = Convert.ToDateTime(DateTime.Now.ToString()).ToString("yyyy-MM-dd");
                    string url = Request.Url.LocalPath;
                    Response.Redirect(url + "?ID=" + MaxID);

                }
                else
                {
                    _qtmgr.UpdateQuestionnaire((int)QSID, (string)surecheck[0][0], (string)surecheck[0][1], Convert.ToDateTime(surecheck[0][2]), Convert.ToDateTime(surecheck[0][3]), (byte)surecheck[0][4]);
                }

                this.lblmsgSure.Text = "※  儲存成功";
            }
            else
                this.lblmsgSure.Text = "※  資料有誤，或空白請再次確認";
        }


        public List<ArrayList> SureCheck(int tabcontent)
        {
            if (tabcontent == 1)
            {
                string quTitle = this.TextBox1.Text.Trim();
                string quDescribe = this.TextBox2.Text.Trim();
                string quStartTime = this.TextBox3.Text.Trim();
                string quEndTime = this.TextBox4.Text.Trim();
                bool quopen = this.chkopen.Checked;

                string[] values = { quTitle, quDescribe, quStartTime, quEndTime };
                foreach (string value in values)
                {
                    if (string.IsNullOrWhiteSpace(value))
                    {
                        return new List<ArrayList>();
                    }
                }

                DateTime DquStartTime = Convert.ToDateTime(quStartTime);
                DateTime DquEndTime = Convert.ToDateTime(quEndTime);
                if (DquStartTime >= DquEndTime)
                    return new List<ArrayList>();

                byte bytequopen = 1;
                if (!quopen)
                    bytequopen = 0;

                List<ArrayList> lists = new List<ArrayList>();
                ArrayList arrayList = new ArrayList() {
                    quTitle, quDescribe, DquStartTime, DquEndTime, bytequopen
                };
                lists.Add(arrayList);
                return lists;
            }

            if (tabcontent == 2)
            {
                List<ArrayList> lists = new List<ArrayList>();
                List<int> ID = new List<int>();
                foreach (string joinsession in _joinsessions)
                {
                    if (this.Session[joinsession] != null)
                    {
                        string[] data = this.Session[joinsession].ToString().Split(' ');

                        if (data.Last() == "100")
                        {
                            //ID QuestionnaireID, title, answer, qtype, required, TheMarkIsisNew
                            ArrayList list = new ArrayList()
                            {
                                data[1], data[2], data[3], data[4], data[5], data[0] // QuestionnaireID, title, answer, qtype, required, 新ID
                            };
                            lists.Add(list);
                        }
                        else if (data.Last() == "1")
                        {
                            ArrayList list = new ArrayList()
                            {
                                data[1], data[2], data[3], data[4], data[5], data[0]  // QuestionnaireID, title, answer, qtype, required, 原ID
                            };
                            lists.Add(list);
                        }
                    }
                }

                return lists;
            }

            return new List<ArrayList>();
        }


        protected void btnjoin_Click(object sender, EventArgs e)
        {
            //----------------防呆判斷-----------------
            bool joincheck = true;
            //問題上限個
            int sessioncount = 0;
            foreach (string joinsession in _joinsessions)
            {
                if (this.Session[joinsession] != null)
                    sessioncount += 1;
            }
            if (sessioncount == _joinsessions.Length)
            {
                this.Session["litmsgSureT"] = $"※  問題上限{_joinsessions.Length}個";
                joincheck = false;
            }

            string qtitle = this.TextBox5.Text;
            string qanswer = this.TextBox7.Text;
            if (string.IsNullOrEmpty(qtitle) || string.IsNullOrEmpty(qanswer))
            {
                this.Session["litmsgSureT"] = "※  欄位不能空白";
                joincheck = false;
            }

            if (qtitle.Contains(' ') || qanswer.Contains(' '))
            {
                this.Session["litmsgSureT"] = "※  欄位內不能含有空白符號";
                joincheck = false;
            }

            if (joincheck)
            {
                //----------------重新排序Session ID-----------------
                int newID = SortNewJoinSessionID();

                //----------------按加入後把值放入Session中-----------------
                string TheMarkIsisNew = "100";
                string QuestionnaireID = Request.QueryString["ID"];
                string title = this.TextBox5.Text.Trim();
                string answer = this.TextBox7.Text.Trim();
                string qtypeSelected = this.DropDownList2.SelectedValue;
                string requiredChecked = this.CheckBox1.Checked.ToString();
                string qtype = "3";
                if (qtypeSelected == "單選方塊")
                    qtype = "1";
                else if (qtypeSelected == "複選方塊")
                    qtype = "2";
                string required = "0";
                if (requiredChecked == "True")
                    required = "1";

                List<string> sessionquestion = new List<string>(){
               QuestionnaireID, title, answer, qtype, required, TheMarkIsisNew
            };

                for (int i = 0; i < _joinsessions.Length; i++)
                {
                    if (this.Session[_joinsessions[i]] == null)
                    {
                        newID += 1;
                        int NewJoinID = newID;
                        sessionquestion.Insert(0, NewJoinID.ToString());
                        this.Session[_joinsessions[i]] = String.Join(" ", sessionquestion);
                        break;
                    }
                }
            }

            Response.Redirect(Request.RawUrl + "#tab-2");
        }


        protected void btndelete_Click(object sender, EventArgs e)
        {
            //TheMarkIsisNew(session[5]): 0是從資料庫抓出並被按刪除; 1是從資料庫抓出; 100是新加入的的問題
            string[] vals = this.Request.Form.GetValues("questionlistcheck");
            if (vals != null)
            {
                foreach (string val in vals)
                {

                    foreach (string joinsession in _joinsessions)
                    {
                        if (this.Session[joinsession] != null)
                        {
                            string[] Sessiondata = this.Session[joinsession].ToString().Split(' ');
                            if (Sessiondata[0] == val && Sessiondata.Last() == "100")
                            {
                                this.Session[joinsession] = null;
                            }
                            else if (Sessiondata[0] == val && Sessiondata.Last() == "1")
                            {
                                Sessiondata[6] = "0";
                                this.Session[joinsession] = String.Join(" ", Sessiondata);
                            }
                        }
                    }
                }

                SortNewJoinSessionID();
            }

            Response.Redirect(Request.RawUrl + "#tab-2");

        }

        /// <summary>
        /// 加入跟刪除時，為了避免按加入或刪除時亂插入Session中
        /// </summary>
        /// <returns>迴傳:按加入後給最新的ID的最後一筆的ID序號</returns>
        public int SortNewJoinSessionID()
        {
            //----------------避免按加入時亂插入Session中-----------------
            //
            int newID = 100;
            //重新排序新加入的Session ID後，並全部把有值的Session加入空list中
            List<string> sortsessions = new List<string>();
            for (int i = 0; i < _joinsessions.Length; i++)
            {
                if (this.Session[_joinsessions[i]] != null)
                {
                    //重新排序ID
                    string[] splitjoinsession = this.Session[_joinsessions[i]].ToString().Split(' ');
                    if (splitjoinsession.Last() == "100")
                    {
                        newID += 1;
                        splitjoinsession[0] = newID.ToString();

                        this.Session[_joinsessions[i]] = String.Join(" ", splitjoinsession);
                    }

                    sortsessions.Add((string)this.Session[_joinsessions[i]]);
                    this.Session[_joinsessions[i]] = null;
                }
            }

            //重新排序新加入ID後，依序把值放回去sessions中
            for (int i = 0; i < sortsessions.Count; i++)
            {
                this.Session[_joinsessions[i]] = sortsessions[i];
            }
            return newID;
        }

        protected void Repeater1_ItemCommand(object source, RepeaterCommandEventArgs e)
        {
            //把Session裡有值的ID都先存起來
            List<string> SessionIDs = new List<string>();
            foreach (string joinsession in _joinsessions)
            {
                if (this.Session[joinsession] != null)
                {
                    string[] sessiondata = this.Session[joinsession].ToString().Split();
                    SessionIDs.Add(sessiondata[0]);
                }
            }

            //用有ID的值下去比對ItemCommand，比對到的就新增Session["editsession"]，再Page_Load做處理即可
            foreach (string SessionID in SessionIDs)
            {
                if (e.CommandName == "questionedit" + SessionID)
                {
                    foreach (string joinsession in _joinsessions)
                    {
                        if (this.Session[joinsession] != null)
                        {
                            string[] sessiondata = this.Session[joinsession].ToString().Split();
                            if (sessiondata[0] == SessionID)
                            {
                                this.Session["editsession"] = joinsession;
                            }

                        }

                    }
                }
            }

            Response.Redirect(Request.RawUrl + "#tab-2");

        }

        protected void btnSure2_Click(object sender, EventArgs e)
        {
            Dictionary<int, int> dic = new Dictionary<int, int>();
            //QuestionnaireID, title, answer, qtype, required, ID
            List<ArrayList> surechecks = SureCheck(2);

            if (surechecks.Count != 0)
            {
                _qmgr.delQuestion(Convert.ToInt32(surechecks[0][0]));

                foreach (ArrayList surecheck in surechecks)
                {
                    //int ID = Convert.ToInt32(surecheck[5]);
                    int QuestionnaireID = Convert.ToInt32(surecheck[0]);
                    string title = surecheck[1].ToString();
                    string answer = surecheck[2].ToString();
                    int qtype = Convert.ToInt32(surecheck[3]);
                    byte required = Convert.ToByte(surecheck[4].ToString() == "True" ? 1 : 0);
                    _qmgr.insertQuestion(QuestionnaireID, title, answer, qtype, required);

                    //如果以填寫過的問卷也要可以修改的話用以下方式
                    //if (ID < 100)
                    //{
                    //    _qmgr.insertQuestion(QuestionnaireID, title, answer, qtype, required, out int newQuestionid);

                    //    _qmgr.updateAnswer(ID, newQuestionid);
                    //}
                    //else
                    //    _qmgr.insertQuestion(QuestionnaireID, title, answer, qtype, required, out int newQuestionid);

                }
                this.Session["litmsgSureT"] = "※  儲存成功";
            }
            else
                this.Session["litmsgSureT"] = "※  資料有誤，或空白請再次確認";

            Response.Redirect(Request.RawUrl + "#tab-2");
        }

        protected void btnCancel2_Click(object sender, EventArgs e)
        {

            foreach (string joinsession in _joinsessions)
            {
                this.Session[joinsession] = null;
            }
            this.Session["editsession"] = null;
            this.Session["litmsgSureT"] = null;
            Response.Redirect("/index.aspx/backindex");

        }


        //======================▼這裡前臺填寫問捲也要用到，可抽成方法(但懶惰我就用複製的了)============================

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


                    string writedQusetionnaire = "NO";
                    if (this.Session[QTypeID] != null)
                    {
                        writedQusetionnaire = this.Session[QTypeID].ToString();
                    }


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


        private void RadioButtonListcreate(string num, int ID, string title, string answertotal, int writedPage)
        {
            Label lbl = new Label();
            lbl.Text = "<p>" + num + title + "</p>";
            lbl.ID = "msg" + ID;
            lbl.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lbl);

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

            this.PlaceHolder3.Controls.Add(rdolist);
        }
        private void RadioButtonListwrited(string num, int ID, string title, string answertotal, string writedQusetionnaire, int writedPage)
        {
            Label lbl = new Label();
            lbl.Text = "<p>" + num + title + "</p>";
            lbl.ID = "msg" + ID;
            lbl.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lbl);

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

            this.PlaceHolder3.Controls.Add(rdolist);
        }


        private void CheckBoxListcreate(string num, int ID, string title, string answertotal, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "</p>";
            lit.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lit);

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

            this.PlaceHolder3.Controls.Add(cblist);
        }
        private void CheckBoxListwrited(string num, int ID, string title, string answertotal, string writedQusetionnaire, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "</p>";
            lit.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lit);

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

            this.PlaceHolder3.Controls.Add(cblist);
        }


        private void TextBoxcreate(string num, int ID, string title, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "<p>";
            lit.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lit);

            TextBox txt = new TextBox();
            txt.ID = "txt" + ID;
            txt.CssClass = "input-txtinput";
            if (writedPage == 1)
                txt.ReadOnly = true;
            this.PlaceHolder3.Controls.Add(txt);
        }
        private void TextBoxwrited(string num, int ID, string title, string writedQusetionnaire, int writedPage)
        {
            Label lit = new Label();
            lit.Text = "<p>" + num + title + "<p>";
            lit.CssClass = "input-title";
            this.PlaceHolder3.Controls.Add(lit);

            TextBox txt = new TextBox();
            txt.ID = "txt" + ID;
            txt.CssClass = "input-txtinput";
            txt.Text = writedQusetionnaire;

            if (writedPage == 1)
                txt.ReadOnly = true;

            this.PlaceHolder3.Controls.Add(txt);
        }


        //======================▲這裡前臺填寫問捲也要用到，可抽成方法(但懶惰我就用複製的了)============================

        protected void Repeater2_ItemCommand(object source, RepeaterCommandEventArgs e)
        {
            if (e.CommandName == "btnAnswer")
            {
                string editpostid = e.CommandArgument.ToString();
                this.Session["btnAnswer"] = editpostid;
                this.Session["questionshow"] = 1;
                Response.Redirect(Request.RawUrl + "#tab-3");
            }
        }


        protected void Repeater3_ItemDataBound(object sender, RepeaterItemEventArgs e)
        {
            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);

            List<Question> QuestionData = _Smgr.GetmanageQuestion((int)QSID, 1);

            int numquestion = QuestionData[Questionnum].ID;
            List<StatisticsData> StatisticsDatas = _Smgr.GetStatistics((int)QSID, 1, numquestion);

            string[] answerlist = QuestionData[Questionnum].Answer.Split(';');  //12~15;16~18;19~22;23~30;30~40

            List<StatisticsData> StatisticShows = new List<StatisticsData>();

            foreach (string answer in answerlist)
            {
                StatisticsData StatisticShow = new StatisticsData()
                {
                    S_ID = QuestionData[Questionnum].QuestionnaireID,
                    S_Title = QuestionData[Questionnum].Title,
                    S_Answer = answer,
                };
                StatisticShows.Add(StatisticShow);
            }


            int totalcount = 0;
            foreach (StatisticsData StatisticsData in StatisticsDatas)
            {
                foreach (StatisticsData answerdataplus in StatisticShows)
                {
                    if (StatisticsData.Answer == answerdataplus.S_Answer)
                    {
                        //{19~22:1}
                        answerdataplus.S_Answer = StatisticsData.Answer;
                        answerdataplus.S_Count = StatisticsData.Count.ToString();
                        totalcount += StatisticsData.Count;
                    }
                }
            }


            foreach (StatisticsData answerdataplus in StatisticShows)
            {
                string answercount = answerdataplus.S_Count; //12~15;16~18;19~22;23~30;30~40

                if (answercount != null)  //19~22:1
                {
                    string ratio = ((100 / totalcount) * Convert.ToInt32(answerdataplus.S_Count) + 1).ToString() + "%";
                    answerdataplus.S_Rate = ratio;
                }
                else
                {
                    answerdataplus.S_Rate = "0%";
                    answerdataplus.S_Count = "0";
                }
            }

            if (e.Item.ItemType == ListItemType.Item ||
               e.Item.ItemType == ListItemType.AlternatingItem)
            {
                Repeater rptSubsection = e.Item.FindControl("Repeater4") as Repeater;
                rptSubsection.DataSource = StatisticShows;
                rptSubsection.DataBind();
                Questionnum += 1;
            }
        }


        protected void Repeater5_ItemDataBound(object sender, RepeaterItemEventArgs e)
        {
            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);

            List<Question> QuestionData2 = _Smgr.GetmanageQuestion((int)QSID, 2);

            int numquestion = QuestionData2[QuestionnumTwo].ID;
            List<StatisticsData> StatisticsDatas = _Smgr.GetStatisticsTwo((int)QSID, 2, numquestion);

            string[] answerlist = QuestionData2[QuestionnumTwo].Answer.Split(';');
            //活存/定存;儲蓄險;外幣存款;債券;ETF;信託基金;股票;房地產;外匯;虛擬貨幣

            List<StatisticsData> StatisticShows = new List<StatisticsData>();

            foreach (string answer in answerlist)
            {
                StatisticsData StatisticShow = new StatisticsData()
                {
                    S_ID = QuestionData2[QuestionnumTwo].ID,
                    S_Title = QuestionData2[QuestionnumTwo].Title,
                    S_Answer = answer,
                    S_Count = "0",
                };
                StatisticShows.Add(StatisticShow);
            }

            int totalcount = 0;
            foreach (StatisticsData StatisticsData in StatisticsDatas) //SQL
            {
                string[] datas = StatisticsData.Answer.Split(',');

                foreach (string data in datas)
                {
                    foreach (StatisticsData StatisticShow in StatisticShows)
                    {
                        if (data == StatisticShow.S_Answer)
                        {
                            int scount = Convert.ToInt32(StatisticShow.S_Count);
                            StatisticShow.S_Count = (scount + 1).ToString();
                            totalcount += 1;
                        }
                    }
                }

            }


            foreach (StatisticsData answerdataplus in StatisticShows)
            {
                string answercount = answerdataplus.S_Count;

                if (answercount != "0")
                {
                    string ratio = ((100 / totalcount) * Convert.ToInt32(answerdataplus.S_Count)).ToString() + "%";
                    answerdataplus.S_Rate = ratio;
                }
                else
                {
                    answerdataplus.S_Rate = "0%";
                    answerdataplus.S_Count = "0";
                }
            }



            if (e.Item.ItemType == ListItemType.Item || e.Item.ItemType == ListItemType.AlternatingItem)
            {
                Repeater rptSubsection = e.Item.FindControl("Repeater6") as Repeater;
                rptSubsection.DataSource = StatisticShows;
                rptSubsection.DataBind();
                QuestionnumTwo += 1;
            }



        }


        //private void WriteToCSV(string FilePath, AnswerData info, List<Question> answer)
        //{
        //    using (var file = new StreamWriter(FilePath))
        //    {
        //        //Person info
        //        file.WriteLineAsync($"{"姓名"},{"年齡"},{"手機"},{"信箱"},{"填寫日期"}");
        //        file.WriteLineAsync($"{info.Name},{info.Age},{info.Phone},{info.Email},{info.Date}");

        //        file.WriteLineAsync($"{" "},{" "},{" "},{" "},{" "}");

        //        //Person answer
        //        file.WriteLineAsync($"{"問題"},{"回答"},{"選擇"},{"種類"},{"必填"}");
        //        foreach (var item in answer)
        //        {
        //            file.WriteLineAsync($"{item.Title},{item.Answer},{item.Choose},{item.QType},{item.Required}");
        //        }
        //        file.WriteLineAsync($"{" "},{" "},{" "},{" "},{" "}");
        //        file.WriteLineAsync($"{" "},{" "},{" "},{" "},{" "}");
        //    }
        //}

        protected void inputCSV_Click(object sender, EventArgs e)
        {
            this.Session["tag3"] = null;

            int? QSID = Convert.ToInt32(Request.QueryString["ID"]);
            if (QSID != null && QSID != 0)
            {
                List<AnswerData> infos = _qtmgr.GetBackPersonalallinfo((int)QSID);

                string FilePath = @"D:\OneDrive\文件\GitHubFile\Program_Practice\C#\Questionnaire\Questionnaire\info.csv";
                if (this.TextBox11.Text != "")
                    FilePath = this.TextBox11.Text;

                try
                {
                    using (var file = new StreamWriter(FilePath))
                    {
                        foreach (AnswerData info in infos)
                        {
                            //Person info
                            file.WriteLine($"{"姓名"},{"年齡"},{"手機"},{"信箱"},{"填寫日期"}");
                            file.WriteLine($"{info.Name},{info.Age},{info.Phone},{info.Email},{info.Date}");

                            file.WriteLine($"{"*****"},{"*****"},{"*****"},{"*****"},{"*****"}");

                            //Person answer

                            List<Question> answers = _qtmgr.GetBackPersonalallanswer(info.ID, (int)QSID);

                            file.WriteLine($"{"問題"},{"回答"},{"選擇"},{"種類"},{"必填"}");
                            foreach (var item in answers)
                            {
                                file.WriteLine($"{item.Title},{item.Answer},{item.Choose},{item.QType},{item.Required}");
                            }
                            file.WriteLine($"{"=============="},{"============"},{"============"},{"============"},{"============"}");
                            file.WriteLine($"{" "},{" "},{" "},{" "},{" "}");
                        }
                    }

                }
                catch
                {
                    this.Session["tag3"] = "儲存路徑不正確";
                }

            }
            else
                this.Session["tag3"] = "無此資料";

            Response.Redirect(Request.RawUrl + "#tab-3");
        }

        protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int ID = Convert.ToInt32(this.DropDownList1.SelectedValue);

            Question Asked = _famgr.GetmanageFrequentlyAskedOne(ID);

            this.Session["editsession"] = $"{Asked.ID} {"Asked"} {Asked.Title} {Asked.Answer} {Asked.QType} {Asked.Required} 1";

            Response.Redirect(Request.RawUrl + "#tab-2");


            //this.TextBox5.Text = Asked.Title;
            //this.TextBox7.Text = Asked.Answer;

            //int AskedQtype = Asked.QType;
            //if (AskedQtype == 1)
            //    this.DropDownList2.SelectedValue = "單選方塊";
            //else if (AskedQtype == 2)
            //    this.DropDownList2.SelectedValue = "複選方塊";
            //else
            //    this.DropDownList2.SelectedValue = "文字";

            //if (Asked.Required == true)
            //    this.CheckBox1.Checked = true;
        }
    }
}