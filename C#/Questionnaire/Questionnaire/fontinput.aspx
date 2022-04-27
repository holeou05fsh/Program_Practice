<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="fontinput.aspx.cs" Inherits="Questionnaire.fontinput" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>fontinput</title>
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
                    <asp:Literal ID="lilTimestate" runat="server"></asp:Literal>
                    <br />
                    <asp:Literal ID="lilStartTime" runat="server"></asp:Literal>
                    ~ 
                    <asp:Literal ID="lilEndTime" runat="server"></asp:Literal>

                </div>
            </div>
        </div>

        <div class="input-head">
            <h2>
                <asp:Literal ID="lilTitle" runat="server"></asp:Literal>
            </h2>
            <p>
                <asp:Literal ID="lilDescribe" runat="server"></asp:Literal>
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
                            <th>手機</th>
                            <td>
                                <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <th>Email</th>
                            <td>
                                <asp:TextBox ID="TextBox3" runat="server" TextMode="Email"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <th>年齡</th>
                            <td>
                                <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                    </table>

                    <div class="input-button">
                        <asp:Literal ID="litmsg" runat="server"></asp:Literal>
                        <h3>
                            <asp:Literal ID="litqustioncount" runat="server"></asp:Literal>
                        </h3>
                        <asp:Button ID="btnCancel" runat="server" Text="取消" OnClick="btnCancel_Click" />
                        <asp:Button ID="btnSure" runat="server" Text="確定" OnClick="btnSure_Click" />
                    </div>
                </div>

            </div>


        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder2" runat="server" Visible="false">
            <div class="Questionnaire-input">
                <div class="input-info">
                    <table>
                        <tr>
                            <th>姓名</th>
                            <td>
                                <asp:Literal ID="Literal1" runat="server"></asp:Literal>
                            </td>
                        </tr>
                        <tr>
                            <th>電話</th>
                            <td>
                                <asp:Literal ID="Literal2" runat="server"></asp:Literal>
                            </td>
                        </tr>
                        <tr>
                            <th>EMAIL</th>
                            <td>
                                <asp:Literal ID="Literal3" runat="server"></asp:Literal>
                            </td>
                        </tr>
                        <tr>
                            <th>年齡</th>
                            <td>
                                <asp:Literal ID="Literal4" runat="server"></asp:Literal>
                            </td>
                        </tr>
                    </table>

                    <div class="input-button">
                        <asp:Button ID="btnCancel2" runat="server" Text="取消" OnClick="btnCancel2_Click" />
                        <asp:Button ID="btnSure2" runat="server" Text="確定" OnClick="btnSure2_Click" />
                    </div>
                </div>

            </div>

        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder3" runat="server" Visible="false">
            <div class="Questionnaire-input">
                <div class="input-radio">

                    <asp:Repeater ID="Repeater1" runat="server" OnItemDataBound="Repeater1_OnItemDataBound">
                        <ItemTemplate>
                            <h3>
                                <%# Eval("Title") %>
                            </h3>

                            <asp:Repeater ID="Repeater2" runat="server">
                                <ItemTemplate>
                                    <p class="input-answer"><%# Eval("S_Answer") %></p>
                                    <div class="input-show">

                                        <div class="input-barchart" style="width: <%#Eval("S_Rate") %>;">
                                            <p><%#Eval("S_Rate") %>  (<%#Eval("S_Count") %>人)</p>
                                        </div>

                                    </div>
                                </ItemTemplate>
                            </asp:Repeater>

                        </ItemTemplate>

                        <SeparatorTemplate>
                            <hr />
                        </SeparatorTemplate>
                        <HeaderTemplate>
                            <h1>單選方塊</h1>
                            <hr />
                        </HeaderTemplate>
                    </asp:Repeater>

                </div>

                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <div class="input-radio">

                    <asp:Repeater ID="Repeater3" runat="server" OnItemDataBound="Repeater3_ItemDataBound">
                        <ItemTemplate>
                            <h3>
                                <%# Eval("Title") %>
                            </h3>

                            <asp:Repeater ID="Repeater4" runat="server">
                                <ItemTemplate>
                                    <p class="input-answer"><%# Eval("S_Answer") %></p>
                                    <div class="input-show">

                                        <div class="input-barchart" style="width: <%#Eval("S_Rate") %>;">
                                            <p><%#Eval("S_Rate") %>  (<%#Eval("S_Count") %>人)</p>
                                        </div>

                                    </div>
                                </ItemTemplate>

                            </asp:Repeater>

                        </ItemTemplate>

                        <SeparatorTemplate>
                            <hr />
                        </SeparatorTemplate>
                        <HeaderTemplate>
                            <h1>複選方塊</h1>
                            <hr />
                        </HeaderTemplate>
                    </asp:Repeater>

                </div>


                <div class="input-button">
                    <asp:Button ID="btnSure3" runat="server" Text="確定" OnClick="btnSure3_Click" />
                </div>
            </div>
        </asp:PlaceHolder>

    </form>
</body>
</html>
