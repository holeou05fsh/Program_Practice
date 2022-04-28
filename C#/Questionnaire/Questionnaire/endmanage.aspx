<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="endmanage.aspx.cs" Inherits="Questionnaire.endmanage" %>

<%@ Register Src="~/ShareControls/ucPagination.ascx" TagPrefix="uc1" TagName="ucPagination" %>


<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>endmanage</title>
    <link href="/CSS/endmanage.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">

        <h1>後台-問卷管理</h1>
        <div class="managemain">

            <div class="left">
                <div class="managelink">
                    <oi>
                        <li><a href="/index.aspx/backindex">問卷管理</a> </li>
                        <li><a href="/index.aspx/frequentlyasked">常用問題管理</a> </li>
                    </oi>
                </div>
            </div>

            <div class="right">
                <div>
                    <span id="tab-1"></span>
                    <span id="tab-2"></span>
                    <span id="tab-3"></span>
                    <span id="tab-4"></span>

                    <!-- 頁籤按鈕 -->
                    <div id="tab">
                        <ul>
                            <li><a href="#tab-1">問卷</a></li>
                            <li><a href="#tab-2">問題</a></li>
                            <li><a href="#tab-3">填寫資料</a></li>
                            <li><a href="#tab-4">統計</a></li>
                        </ul>

                        <!-- 頁籤的內容區塊 -->
                        <div class="tab-content-1">
                            <table>
                                <tr>
                                    <th>問卷名稱</th>
                                    <td>
                                        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox></td>
                                </tr>
                                <tr>
                                    <th>描述內容</th>
                                    <td>
                                        <asp:TextBox ID="TextBox2" runat="server" TextMode="MultiLine" Columns="60" Rows="5"></asp:TextBox></td>
                                </tr>
                                <tr>
                                    <th>開始時間</th>
                                    <td>
                                        <asp:TextBox ID="TextBox3" runat="server" TextMode="Date"></asp:TextBox></td>
                                </tr>
                                <tr>
                                    <th>結束時間</th>
                                    <td>
                                        <asp:TextBox ID="TextBox4" runat="server" TextMode="Date"></asp:TextBox></td>
                                </tr>
                                <tr>
                                    <th></th>
                                    <td>
                                        <asp:CheckBox ID="chkopen" runat="server" Text="已開啟" Checked="true" />
                                    </td>
                                </tr>
                            </table>

                            <div class="input-button">
                                <asp:Button ID="btnCancel" runat="server" Text="取消" OnClick="btnCancel_Click" />
                                <asp:Button ID="btnSure" runat="server" Text="送出" OnClick="btnSure_Click" />
                            </div>
                            <asp:Literal ID="lblmsgSure" runat="server"></asp:Literal>
                        </div>

                        <div class="tab-content-2">
                            <div class="questioninput">
                                <table>
                                    <tr>
                                        <th>*注意:</th>
                                        <td>填寫過問卷的，如果在這又修改的話，寫過問卷就對不到ID，所以不能修改!</td>
                                    </tr>
<%--                                    <tr>
                                        <th>*解決:</th>
                                        <td>按送出後，把回答一樣ID的改成新ID即可(但有點懶就這樣吧)</td>
                                    </tr>--%>
                                    <tr>
                                        <th>
                                            <hr />
                                        </th>
                                        <td>
                                            <hr />
                                        </td>
                                    </tr>
                                    <tr>
                                        <th>種類</th>
                                        <td>
                                            <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True"
        onselectedindexchanged="DropDownList1_SelectedIndexChanged">
                                                <asp:ListItem>常用問題</asp:ListItem>
                                            </asp:DropDownList></td>
                                    </tr>
                                    <tr>
                                        <th>問題</th>
                                        <td>
                                            <asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
                                            <asp:DropDownList ID="DropDownList2" runat="server">
                                                <asp:ListItem>單選方塊</asp:ListItem>
                                                <asp:ListItem>複選方塊</asp:ListItem>
                                                <asp:ListItem>文字</asp:ListItem>
                                            </asp:DropDownList>
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
                                <asp:Button ID="btndelete" runat="server" Text="🗑" OnClick="btndelete_Click" />
                                <table class="questionshow">
                                    <tr>
                                        <th></th>
                                        <th>#</th>
                                        <th>問題</th>
                                        <th>種類</th>
                                        <th>必填</th>
                                        <th></th>
                                    </tr>
                                    <asp:Repeater ID="Repeater1" runat="server" OnItemCommand="Repeater1_ItemCommand">
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
                                                    <asp:Button ID="btnedit" runat="server" Text="編輯" CommandName='<%# "questionedit" + Eval("ID").ToString() %>' CommandArgument='<%#Eval("ID") %>' /></td>
                                            </tr>
                                        </ItemTemplate>
                                    </asp:Repeater>

                                </table>
                                <div class="input-button">
                                    <asp:Button ID="btnCancel2" runat="server" Text="取消" OnClick="btnCancel2_Click" />
                                    <asp:Button ID="btnSure2" runat="server" Text="送出" OnClick="btnSure2_Click" />
                                </div>
                            </div>
                            <asp:Literal ID="litmsgSureT" runat="server"></asp:Literal>
                        </div>

                        <div class="tab-content-3">
                            <asp:PlaceHolder ID="PlaceHolder1" runat="server">
                                <asp:Button ID="inputCSV" runat="server" Text="匯出" OnClick="inputCSV_Click" />
                                &nbsp&nbsp&nbsp&nbsp&nbsp
                                <asp:TextBox ID="TextBox11" runat="server" placeholder="請輸入儲存路徑"></asp:TextBox>
                                <asp:Literal ID="Literal2" runat="server"></asp:Literal>
                                <table class="questionshow">
                                    <tr>
                                        <th>#</th>
                                        <th>姓名</th>
                                        <th>填寫時間</th>
                                        <th>觀看細節</th>
                                    </tr>

                                    <asp:Repeater ID="Repeater2" runat="server" OnItemCommand="Repeater2_ItemCommand">
                                        <ItemTemplate>
                                            <tr>
                                                <td><%# Eval("Sort") %></td>
                                                <td><%# Eval("Name") %></td>
                                                <td><%# Eval("Date") %></td>
                                                <td>
                                                    <asp:Button ID="btninfo" runat="server" Text="前往" CommandName="btnAnswer" CommandArgument='<%# Eval("ID") %>' />
                                                </td>
                                            </tr>

                                        </ItemTemplate>
                                    </asp:Repeater>

                                </table>
                                <uc1:ucPagination runat="server" ID="ucPagination" />

                            </asp:PlaceHolder>


                            <asp:PlaceHolder ID="PlaceHolder2" runat="server" Visible="false">

                                <table class="infodata">
                                    <tr>
                                        <td>姓名</td>
                                        <td>
                                            <asp:TextBox ID="TextBox6" runat="server"></asp:TextBox>
                                        </td>
                                        <td>手機</td>
                                        <td>
                                            <asp:TextBox ID="TextBox8" runat="server"></asp:TextBox>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>Email</td>
                                        <td>
                                            <asp:TextBox ID="TextBox9" runat="server"></asp:TextBox>
                                        </td>
                                        <td>年齡</td>
                                        <td>
                                            <asp:TextBox ID="TextBox10" runat="server"></asp:TextBox>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                        <td></td>
                                        <td colspan="2">
                                            <p>
                                                <asp:Literal ID="Literal1" runat="server"></asp:Literal>
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                                <asp:Literal ID="litqustioncount" runat="server"></asp:Literal>

                                <div class="people-answer">
                                    <asp:PlaceHolder ID="PlaceHolder3" runat="server"></asp:PlaceHolder>
                                </div>
                                <asp:Button ID="btnCancel3" runat="server" Text="取消" OnClick="btnCancel3_Click" />
                            </asp:PlaceHolder>
                        </div>

                        <div class="tab-content-4">
                            <asp:Repeater ID="Repeater3" runat="server" OnItemDataBound="Repeater3_ItemDataBound">
                                <ItemTemplate>
                                    <h3>
                                        <%# Eval("Title") %>
                                    </h3>
                                    <asp:Repeater ID="Repeater4" runat="server">
                                        <ItemTemplate>
                                            <p class="input-answer"><%# Eval("S_Answer") %>  <%#Eval("S_Rate") %>  (<%#Eval("S_Count") %>人)</p>
                                        </ItemTemplate>
                                    </asp:Repeater>

                                </ItemTemplate>
                            </asp:Repeater>



                            <asp:Repeater ID="Repeater5" runat="server" OnItemDataBound="Repeater5_ItemDataBound">
                                <ItemTemplate>
                                    <h3>
                                        <%# Eval("Title") %>
                                    </h3>
                                    <asp:Repeater ID="Repeater6" runat="server">
                                        <ItemTemplate>
                                            <p class="input-answer"><%# Eval("S_Answer") %>  <%#Eval("S_Rate") %>  (<%#Eval("S_Count") %>人)</p>
                                        </ItemTemplate>
                                    </asp:Repeater>

                                </ItemTemplate>
                            </asp:Repeater>

                        </div>

                    </div>

                </div>
            </div>
        </div>


    </form>
</body>
</html>
