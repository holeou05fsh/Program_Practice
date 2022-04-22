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
        protected void Page_Load(object sender, EventArgs e)
        {
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