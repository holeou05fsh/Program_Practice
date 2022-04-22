<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="Questionnaire.index" %>

<%@ Register Src="~/ShareControls/ucPagination.ascx" TagPrefix="uc1" TagName="ucPagination" %>


<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>sdf</title>
    <link href="/CSS/index.css" rel="stylesheet" />
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        .fontindex {
            width: 60%;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <asp:Button ID="btnbackindex" runat="server" OnClick="btnbackindex_Click" Text="前後台切換" />
        <asp:Label ID="lblindextitle" runat="server" Text="前台"></asp:Label>


        <asp:PlaceHolder ID="PlaceHolder1" runat="server">

            <div class="Questionnaire-index fontindex">
                <div class="seach">
                    <table>
                        <tr>
                            <td>問卷標題</td>
                            <td colspan="3">
                                <asp:TextBox CssClass="TextBox1" ID="txtkeyword" runat="server"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <td>開始 / 結束</td>
                            <td>
                                <asp:TextBox CssClass="TextBox2" ID="txtStartTime" runat="server" TextMode="Date"></asp:TextBox></td>
                            <td>
                                <asp:TextBox CssClass="TextBox3" ID="txtEndTime" runat="server" TextMode="Date"></asp:TextBox></td>
                            <td>
                                <asp:Button CssClass="TextBox3" ID="btnSearch" runat="server" Text="搜尋" OnClick="btnSearch_Click" /></td>
                        </tr>
                    </table>
                </div>
                <div class="Questionnairelist">


                    <table>
                        <tr>
                            <th style="width: 7%;">#</th>
                            <th style="width: 40%;">問卷</th>
                            <th style="width: 13%;">狀態</th>
                            <th style="width: 16%;">開始時間</th>
                            <th style="width: 16%;">結束時間</th>
                            <th style="width: 25%;">觀看統計</th>
                        </tr>
                        <asp:Repeater ID="Repeater1" runat="server">
                            <ItemTemplate>
                                <tr>
                                    <td><%# Eval("Sort") %></td>
                                    <td><a href="/fontinput.aspx?ID=<%# Eval("ID") %>"><%# Eval("Title") %></a></td>
                                    <td><%# Eval("Timestate") %></td>
                                    <td><%# Eval("StartTime", "{0:yyyy/MM/dd}") %></td>
                                    <td><%# Eval("EndTime", "{0:yyyy/MM/dd}") %></td>
                                    <td><a href="#">前往</a></td>
                                </tr>
                            </ItemTemplate>
                        </asp:Repeater>
                    </table>

                </div>
                <uc1:ucPagination runat="server" id="ucPagination" />
            </div>

        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder2" runat="server" Visible="false">
            <div class="indexmain">

                <div class="left">
                    <div class="indexlink">
                        <oi>
                            <li><a href="#">問卷管理</a> </li>
                            <li><a href="#">常用問題管理</a> </li>
                        </oi>
                    </div>
                </div>

                <div class="right">
                    <div class="Questionnaire-index">
                        <div class="seach">
                            <table>
                                <tr>
                                    <td>問卷標題</td>
                                    <td colspan="3">
                                        <asp:TextBox CssClass="TextBox1" ID="txtkeyword1" runat="server"></asp:TextBox>
                                    </td>
                                </tr>
                                <tr>
                                    <td>開始 / 結束</td>
                                    <td>
                                        <asp:TextBox CssClass="TextBox2" ID="txtStartTime1" runat="server" TextMode="Date" ></asp:TextBox></td>
                                    <td>
                                        <asp:TextBox CssClass="TextBox3" ID="txtEndTime1" runat="server" TextMode="Date"></asp:TextBox></td>
                                    <td>
                                        <asp:Button CssClass="TextBox3" ID="btnSearch1" runat="server" Text="搜尋" OnClick="btnSearch1_Click" /></td>
                                </tr>
                            </table>
                        </div>



                        <div class="Questionnairelist">
                            <div>
                                <asp:Button ID="btndelete" runat="server" Text="🗑" OnClick="btndelete_Click" />
                                <asp:Button ID="btnplus" runat="server" Text="➕" OnClick="btnplus_Click" />
                                <asp:Literal ID="Literal1" runat="server"></asp:Literal>
                            </div>
                            <table>
                                <tr>
                                    <th style="width: 3%;"></th>
                                    <th style="width: 7%;">#</th>
                                    <th style="width: 40%;">問卷</th>
                                    <th style="width: 13%;">狀態</th>
                                    <th style="width: 11%;">開始時間</th>
                                    <th style="width: 11%;">結束時間</th>
                                    <th style="width: 35%;">觀看統計</th>
                                </tr>
                                <asp:Repeater ID="Repeater2" runat="server">
                                    <ItemTemplate>

                                        <tr>
                                            <td>
                                                <input type="checkbox" name="backlistcheck" value='<%# Eval("ID") %>' />
                                            </td>
                                            <td><%# Eval("Sort") %></td>
                                            <td><a href='/endmanage.aspx?ID=<%# Eval("ID") %>'><%# Eval("Title") %></a></td>
                                            <td><%# Eval("StrState") %></td>
                                            <td><%# Eval("StartTime", "{0:yyyy/MM/dd}") %></td>
                                            <td><%# Eval("EndTime", "{0:yyyy/MM/dd}") %></td>
                                            <td><a href="#">前往</a></td>
                                        </tr>
                                    </ItemTemplate>
                                </asp:Repeater>
                            </table>
                        </div>
                        <uc1:ucPagination runat="server" id="ucPagination1" />


                    </div>
                </div>
            </div>
        </asp:PlaceHolder>
        <script>

</script>
    </form>
</body>
</html>
