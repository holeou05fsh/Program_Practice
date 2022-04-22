using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Web;

namespace Questionnaire.Helpers
{
    public class ConfigString
    {
        private const string _MainDB = "DBMain";

        public static string GetConfigString()
        {
            string connString = GetConfigString(ConfigString._MainDB);
            return connString;
        }

        public static string GetConfigString(string name)
        {
            string connString = ConfigurationManager.ConnectionStrings[name].ConnectionString;
            return connString;
        }
    }
}