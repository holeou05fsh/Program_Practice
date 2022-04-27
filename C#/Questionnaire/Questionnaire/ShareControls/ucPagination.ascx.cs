using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Questionnaire.ShareControls
{
    public partial class ucPagination : System.Web.UI.UserControl
    {
        public int PageSize { get; set; } = 4;
        public int PageIndex { get; set; } = 1;
        public int TotalRows { get; set; } = 1;
        public string UrlID { get; set; } = "";

        private string _url = null;
        /// <summary>如果外部有值定URL就使用值定的URL，否則用LocalPath</summary>
        public string Url
        {
            get
            {
                if (this._url == null)
                    return Request.Url.LocalPath;
                else
                    return this._url;
            }
            set
            {
                this._url = value;
            }
        }

        /// <summary>沒有NameValueCollection的狀況，就產生個新空的</summary>
        public void Bind()
        {
            NameValueCollection collection = new NameValueCollection();
            this.Bind(collection);
        }

        /// <summary>如果只有一組參數就直接加入NameValueCollection</summary>
        /// <param name="paramKey"></param>
        /// <param name="paramValue"></param>
        public void Bind(string paramKey, string paramValue)
        {
            NameValueCollection collection = new NameValueCollection();
            collection.Add(paramKey, paramValue);
            this.Bind(collection);
        }

        /// <summary>多參數狀況跑迴圈組字串</summary>
        /// <param name="collection"></param>
        public void Bind(NameValueCollection collection)
        {
            string qsText = this.BuildQueryString(collection);
            string url = this.Url;

            string page = "?Page=";
            if (!String.IsNullOrWhiteSpace(qsText) || url.Contains("?"))
            {
                page = "&Page=";
                var regex = new Regex(Regex.Escape("&"));
                qsText = regex.Replace(qsText, "?", 1);
            }


            int maxpage = (int)Math.Ceiling((decimal)this.TotalRows / this.PageSize);
            this.aLinkPagePrev.HRef = url + qsText + page + (this.PageIndex - 1) + UrlID;
            this.aLinkPageNext.HRef = url + qsText + page + (this.PageIndex + 1) + UrlID;

            if (1 >= this.PageIndex && String.IsNullOrWhiteSpace(qsText)) //|| (1 >= this.PageIndex && String.IsNullOrWhiteSpace(qsText))
                this.aLinkPagePrev.HRef = url + qsText + $"?Page=1" + UrlID;
            else if (1 >= this.PageIndex && !String.IsNullOrWhiteSpace(qsText))
                this.aLinkPagePrev.HRef = url + qsText + $"&Page=1" + UrlID;


            if (maxpage <= this.PageIndex && String.IsNullOrWhiteSpace(qsText)) //maxpage <= this.PageIndex && String.IsNullOrWhiteSpace(qsText)
                this.aLinkPageNext.HRef = url + qsText + $"?Page={maxpage}" + UrlID;
            else if (maxpage <= this.PageIndex && !String.IsNullOrWhiteSpace(qsText))
                this.aLinkPageNext.HRef = url + qsText + $"&Page={maxpage}" + UrlID;

            this.aLinkPage1.HRef = url + qsText + page + "1" + UrlID;
            this.aLinkPage2.HRef = url + qsText + page + "2" + UrlID;
            this.aLinkPage3.HRef = url + qsText + page + "3" + UrlID;
            this.aLinkPage4.HRef = url + qsText + page + "4" + UrlID;
            this.aLinkPage5.HRef = url + qsText + page + "5" + UrlID;


            if (maxpage == 0)
            {
                this.aLinkPagePrev.Visible = false;
                this.aLinkPageNext.Visible = false;
                this.aLinkPage1.Visible = false;
                this.aLinkPage2.Visible = false;
                this.aLinkPage3.Visible = false;
                this.aLinkPage4.Visible = false;
                this.aLinkPage5.Visible = false;
            }
            if (maxpage == 1)
            {
                this.aLinkPage2.Visible = false;
                this.aLinkPage3.Visible = false;
                this.aLinkPage4.Visible = false;
                this.aLinkPage5.Visible = false;
            }

            if (maxpage == 2)
            {
                this.aLinkPage3.Visible = false;
                this.aLinkPage4.Visible = false;
                this.aLinkPage5.Visible = false;
            }

            if (maxpage == 3)
            {
                this.aLinkPage4.Visible = false;
                this.aLinkPage5.Visible = false;
            }

            if (maxpage == 4)
            {
                this.aLinkPage5.Visible = false;
            }
        }

        private string BuildQueryString(NameValueCollection collection)
        {
            List<string> paramList = new List<string>();

            foreach (string key in collection.AllKeys)
            {
                if (collection.GetValues(key) == null)
                    continue;
                else
                {
                    foreach (string val in collection.GetValues(key))
                    {
                        paramList.Add($"&{key}={val}");
                    }
                }
            }
            string result = string.Join("", paramList);
            return result;
        }
    }
}