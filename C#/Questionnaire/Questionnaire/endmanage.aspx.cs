using Questionnaire.Managers;
using Questionnaire.Models;
using System;
using System.Collections;
using System.Collections.Generic;
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
        private string[] _joinsessions = new string[] {
            "joinsession1", "joinsession2", "joinsession3", "joinsession4",
            "joinsession5", "joinsession6", "joinsession7", "joinsession8",
            "joinsession9", "joinsession10", "joinsession11", "joinsession12",
        };

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

                    string[] sessiondata = this.Session[editID].ToString().Split();

                    if (sessiondata.Last() != "1")
                    {
                        this.TextBox5.Text = sessiondata[1];
                        this.TextBox7.Text = sessiondata[2];
                        if (sessiondata[3] == "1")
                            this.DropDownList2.SelectedValue = "單選方塊";
                        else if (sessiondata[3] == "2")
                            this.DropDownList2.SelectedValue = "複選方塊";
                        else
                            this.DropDownList2.SelectedValue = "文字";
                        if (sessiondata[4] == "True")
                            this.CheckBox1.Checked = true;

                        Session[editID] = null;
                        Session["editsession"] = null;
                    }
                    else
                    {
                        this.TextBox5.Text = sessiondata[1];
                        this.TextBox7.Text = sessiondata[2];
                        if (sessiondata[3] == "1")
                            this.DropDownList2.SelectedValue = "單選方塊";
                        else if (sessiondata[3] == "2")
                            this.DropDownList2.SelectedValue = "複選方塊";
                        else
                            this.DropDownList2.SelectedValue = "文字";
                        if (sessiondata[4] == "True")
                            this.CheckBox1.Checked = true;

                        sessiondata[6] = "0";
                        this.Session[editID] = String.Join(" ", sessiondata);
                        this.Session["editsession"] = null;
                    }

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

                    //=========================== Tag-3 ===============================
                    if (Convert.ToInt32(Session["questionshow"]) != 1)
                    {
                        this.PlaceHolder1.Visible = true;
                        this.PlaceHolder2.Visible = false;
                    }
                    else
                    {
                        this.PlaceHolder1.Visible = false;
                        this.PlaceHolder2.Visible = true;
                    }
                }

            }
        }
        protected void btnCancel3_Click(object sender, EventArgs e)
        {
            Session["questionshow"] = 0;
            Response.Redirect("/endmanage.aspx#tab-3");
        }

        protected void btninfo_Click(object sender, EventArgs e)
        {
            Session["questionshow"] = 1;
            Response.Redirect("/endmanage.aspx#tab-3");
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
                                data[1], data[2], data[3], data[4], data[5]
                            };
                            lists.Add(list);
                        }
                        else if (data.Last() == "1")
                        {
                            ArrayList list = new ArrayList()
                            {
                                data[1], data[2], data[3], data[4], data[5]
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
                if (this.Session[joinsession] == null)
                    sessioncount += 1;
            }
            if (sessioncount == 12)
            {
                this.Session["litmsgSureT"] = "※  問題上限12個";
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
            if (!IsPostBack)
            {

            }
            //QuestionnaireID, title, answer, qtype, required
            List<ArrayList> surechecks = SureCheck(2);

            if (surechecks.Count !=0)
            {
                _qmgr.delQuestion(Convert.ToInt32(surechecks[0][0]));

                foreach (ArrayList surecheck in surechecks)
                {
                    int QuestionnaireID = Convert.ToInt32(surecheck[0]);
                    string title = surecheck[1].ToString();
                    string answer = surecheck[2].ToString();
                    int qtype = Convert.ToInt32(surecheck[3]);
                    byte required = Convert.ToByte(surecheck[4].ToString() == "True" ? 1 : 0);
                    _qmgr.insertQuestion(QuestionnaireID, title, answer, qtype, required);
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
    }
}