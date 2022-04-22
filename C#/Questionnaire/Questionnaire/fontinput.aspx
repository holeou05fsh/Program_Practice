<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="fontinput.aspx.cs" Inherits="Questionnaire.fontinput" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>asd</title>
    <link href="/CSS/fontinput.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">


        <div class="container">
            <div class="left-wrapper">
                <div class="one">前台</div>
                <div class="two"></div>
            </div>

            <div class="right-wrapper">
                <div class="three">
                    投票中<br />
                    2021/09/01 ~ 2021/09/01
                </div>
            </div>
        </div>

        <div class="input-head">
            <h2>青春洋溢高中生頭票</h2>
            <p>
                the sequence of numbers assigned to pages in a book or periodical.
                later editions are identical in text and pagination
                the sequence of numbers assigned to pages in a book or periodical.
                later editions are identical in text and pagination
            </p>
        </div>

        <asp:PlaceHolder ID="PlaceHolder1" runat="server">
            <div class="Questionnaire-input">
                <div class="input-info">
                    <table>
                        <tr>
                            <th>姓名</th>
                            <td>
                                <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <th>姓名</th>
                            <td>
                                <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <th>姓名</th>
                            <td>
                                <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <th>姓名</th>
                            <td>
                                <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                    </table>
                </div>

                <div class="input-radio">
                    <ol>
                        <li>請投給以下一位</li>
                    </ol>

                    <asp:RadioButtonList ID="rdoinput" runat="server">
                        <asp:ListItem>Item 1</asp:ListItem>
                        <asp:ListItem>Item 2</asp:ListItem>
                        <asp:ListItem>Item 3</asp:ListItem>
                        <asp:ListItem>Item 4</asp:ListItem>
                    </asp:RadioButtonList>

                </div>
            </div>

            <div class="input-button">
                <h3>共1個問題</h3>
                <asp:Button ID="btnCancel" runat="server" Text="取消" onclick="btnCancel_Click" />
                <asp:Button ID="btnSure" runat="server" Text="確定" onclick="btnSure_Click" />
            </div>
        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder2" runat="server" Visible="false">
            <div class="Questionnaire-input">
                <div class="input-info">
                    <table>
                        <tr>
                            <th>姓名</th>
                            <td>測試者</td>
                        </tr>
                        <tr>
                            <th>電話</th>
                            <td>電話</td>
                        </tr>
                        <tr>
                            <th>EMAIL</th>
                            <td>EMAIL</td>
                        </tr>
                        <tr>
                            <th>年齡</th>
                            <td>21</td>
                        </tr>
                    </table>
                </div>
                <div class="input-radio">
                    <ol>
                        <li>請投給以下一位</li>
                    </ol>
                    <p class="input-answer">核廢料(dsfdsf)</p>

                </div>
            </div>
            <div class="input-button">
                <asp:Button ID="btnCancel2" runat="server" Text="取消" onclick="btnCancel2_Click" />
                <asp:Button ID="btnSure2" runat="server" Text="確定" onclick="btnSure2_Click" />
            </div>
        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder3" runat="server" Visible="false">
            <div class="Questionnaire-input">
                <div class="input-radio">
                    <ol>
                        <li>請投給以下一位</li>
                    </ol>

                    <p class="input-answer">核廢料(dsfdsf)</p>
                    <div class="input-show">
                        <div class="input-barchart" style="width: 60%;"><p>60%  (3245人)</p></div>
                    </div>

                    <p class="input-answer">核廢料(dsfdsf)</p>

                    <div class="input-show">
                        <div class="input-barchart" style="width: 40%;"><p>40%  (245人)</p></div>
                    </div>

                    <p class="input-answer">核廢料(dsfdsf)</p>
                    <div class="input-show">
                        <div class="input-barchart" style="width: 0%;"><p>0%  (0人)</p></div>
                    </div>
                </div>
                <div class="input-button">
                <asp:Button ID="btnSure3" runat="server" Text="確定" onclick="btnSure3_Click" />
            </div>
            </div>
        </asp:PlaceHolder>

    </form>
</body>
</html>
