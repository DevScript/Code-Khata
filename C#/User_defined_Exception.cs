using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace userdefined_Exception
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int a = CheckAge();
                Console.WriteLine(a);
                Console.ReadLine();
            }
            catch (UserDefinedEX_AGE ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        static int CheckAge()
        {
            Console.WriteLine(" ---Enter AGE--- ");
            int age = Convert.ToInt32(Console.ReadLine());
            if (age <= 0)
            {
                throw new Exception("Age should be POSITIVE or at least Greater than 0");
            }
            return age;
        }

        public class UserDefinedEX_AGE : Exception
        {
            public UserDefinedEX_AGE(string msg) : base(msg)
            {

            }
        }
    }
}
