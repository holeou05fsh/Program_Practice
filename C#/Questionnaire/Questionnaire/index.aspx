<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="Questionnaire.index" %>

<%@ Register Src="~/ShareControls/ucPagination.ascx" TagPrefix="uc1" TagName="ucPagination" %>


<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>index</title>
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
                                    <td><a href="/fontinput.aspx?ID=<%# Eval("ID") + "&page=3"%>">前往</a></td>
                                </tr>
                            </ItemTemplate>
                        </asp:Repeater>
                    </table>

                </div>
                <uc1:ucPagination runat="server" ID="ucPagination" />
            </div>

        </asp:PlaceHolder>

        <asp:PlaceHolder ID="PlaceHolder2" runat="server" Visible="false">
            <div class="indexmain">

                <div class="left">
                    <div class="indexlink">
                        <oi>
                            <li><a href="/index.aspx/backindex">問卷管理</a> </li>
                            <li><a href="/index.aspx/frequentlyasked">常用問題管理</a> </li>
                        </oi>
                    </div>
                </div>

                <asp:PlaceHolder ID="PlaceHolder3" runat="server">
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
                                            <asp:TextBox CssClass="TextBox2" ID="txtStartTime1" runat="server" TextMode="Date"></asp:TextBox></td>
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
                                                <td><a href='/endmanage.aspx?ID=<%# Eval("ID") %>#tab-4'>前往</a></td>
                                            </tr>
                                        </ItemTemplate>
                                    </asp:Repeater>
                                </table>
                            </div>
                            <uc1:ucPagination runat="server" ID="ucPagination1" />


                        </div>
                    </div>
                </asp:PlaceHolder>

                <asp:PlaceHolder ID="PlaceHolder4" runat="server" Visible="false">
                    <div class="right asked">
                        <div>
                            <span id="tab-1">主頁</span>

                            <!-- 頁籤按鈕 -->
                            <div id="tab">
                                <ul>
                                    <li><a href="#tab-1">常用問卷</a></li>
                                </ul>

                                <!-- 頁籤的內容區塊 -->
                                <div class="tab-content-1">

                                    <div class="questioninput">
                                        <table>
                                            <tr>
                                                <th>問題</th>
                                                <td>
                                                    <asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
                                                    &nbsp;&nbsp; 
                                                    <asp:DropDownList ID="DropDownList2" runat="server">
                                                        <asp:ListItem>單選方塊</asp:ListItem>
                                                        <asp:ListItem>複選方塊</asp:ListItem>
                                                        <asp:ListItem>文字</asp:ListItem>
                                                    </asp:DropDownList>
                                                     &nbsp;&nbsp;
                                                    <asp:CheckBox ID="CheckBox1" runat="server" Text="必填" />
                                                </td>
                                            </tr>
                                            <tr>
                                                <th>回答</th>
                                                <td>
                                                    <asp:TextBox ID="TextBox7" runat="server"></asp:TextBox>
                                                    (多個答案以；分隔)
                                                </td>
                                                <td>
                                                    <asp:Button ID="btnjoin" runat="server" Text="加入" OnClick="btnjoin_Click" />
                                                    
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                    <div class="questioninfo">
                                        <asp:Button ID="btndelete1" runat="server" Text="🗑" OnClick="btndelete1_Click"/> 
                                        <table class="questionshow">
                                            <tr>
                                                <th></th>
                                                <th>#</th>
                                                <th>問題</th>
                                                <th>種類</th>
                                                <th>必填</th>
                                                <th></th>
                                            </tr>
                                             <asp:Repeater ID="Repeater3" runat="server" OnItemCommand="Repeater3_ItemCommand">
                                        <ItemTemplate>
                                            <tr>
                                                <td>
                                                    <input type="checkbox" name="questionlistcheck" value='<%# Eval("ID") %>' />
                                                </td>
                                                <td><%# Container.ItemIndex +1%></td>
                                                <td><%# Eval("Title") %></td>
                                                <td><%# Convert.ToInt32(Eval("QType"))==1?"單選方塊":Convert.ToInt32(Eval("QType"))==2?"複選方塊":"文字" %></td>
                                                <td>
                                                    <asp:CheckBox ID="CheckBox3" runat="server" Checked='<%# (bool)Eval("required") %>' onclick="javascript: return false;" />
                                                </td>
                                                <td>
                                                    <asp:Button ID="btnedit" runat="server" Text="編輯" CommandName="questionedit" CommandArgument='<%#Eval("ID")+","+Eval("Title")+","+Eval("Answer")+","+Eval("QType")+","+Eval("Required") %>' /></td>
                                            </tr>
                                        </ItemTemplate>
                                    </asp:Repeater>
                                        </table>
                                    </div>
                                    <asp:Literal ID="litmsgSureT" runat="server"></asp:Literal>
                                </div>


                            </div>

                        </div>
                    </div>
                </asp:PlaceHolder>

            </div>
        </asp:PlaceHolder>
        <script>

</script>
    </form>
</body>
</html>
