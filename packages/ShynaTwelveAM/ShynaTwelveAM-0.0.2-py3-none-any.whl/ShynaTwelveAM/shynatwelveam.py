import os
from ShynaWeather import UpdateWeather
from Shynatime import ShTime
from ShynaTelegramBotNotification import BotNotify
from ShynaDatabase import Shdatabase


class ShynaTwelveAM:
    """
    Process 12 AM task

    1) Update weather to the table for morning greetings
    2) Clean up tables old data.
        a) Shivam_face
        b) Shivam_location
        c) connection_check

    """
    s_weather = UpdateWeather.UpdateWeather()
    s_bot = BotNotify.BotShynaTelegram()
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    result = ''

    def run_at_twelve(self):
        try:
            self.s_weather.update_weather()
            self.clean_tables()
        except Exception as e:
            print(e)
            self.s_bot.message = "Exception at run_at_twelve " + str(e)
            self.s_bot.bot_send_msg_to_master()

    def clean_tables(self):
        try:
            self.s_bot.message = "Initiating Clean up Process"
            self.s_bot.bot_send_msg_to_master()
            delete_date_table = []
            delete_date = self.s_time.subtract_date(from_date=self.s_time.now_date, how_many=7).date()
            # Clean up Shivam_face table
            self.s_data.default_database = os.environ.get('data_db')
            self.s_data.query = "Select count, task_date from shivam_face order by count DESC"
            self.result = self.s_data.select_from_table()
            for item in self.result:
                if self.s_time.string_to_date(date_string=str(delete_date)) > self.s_time.string_to_date(
                        date_string=str(item[1])):
                    delete_date_table.append(item[0])
                else:
                    pass
            if delete_date_table:
                self.s_data.query = "Delete from shivam_face where count IN (" \
                                    "" + str(delete_date_table).replace('[', '').replace(']', '') + " )"
                # print(self.s_data.query)
                self.s_data.create_insert_update_or_delete()
            else:
                print("list is empty")
            # Clean up shivam_device_location table
            delete_date_table = []
            self.result = ''
            self.s_data.default_database = os.environ.get('location_db')
            self.s_data.query = "Select count, new_date from shivam_device_location order by count DESC"
            self.result = self.s_data.select_from_table()
            for item in self.result:
                if self.s_time.string_to_date(date_string=str(delete_date)) > self.s_time.string_to_date(
                        date_string=str(item[1])):
                    delete_date_table.append(item[0])
                else:
                    pass
            if delete_date_table:
                self.s_data.query = "Delete from shivam_device_location where count IN (" \
                                    "" + str(delete_date_table).replace('[', '').replace(']', '') + " )"
                # print(self.s_data.query)
                self.s_data.create_insert_update_or_delete()
            else:
                print("list is empty")
                # Clean up connection_check table
                delete_date_table = []
                self.result = ''
                self.s_data.default_database = os.environ.get('status_db')
                self.s_data.query = "Select count, new_date from connection_check order by count DESC"
                self.result = self.s_data.select_from_table()
                for item in self.result:
                    if self.s_time.string_to_date(date_string=str(delete_date)) > self.s_time.string_to_date(
                            date_string=str(item[1])):
                        delete_date_table.append(item[0])
                    else:
                        pass
                if delete_date_table:
                    self.s_data.query = "Delete from connection_check where count IN (" \
                                        "" + str(delete_date_table).replace('[', '').replace(']', '') + " )"
                    # print(self.s_data.query)
                    self.s_data.create_insert_update_or_delete()
                else:
                    print("list is empty")
        except Exception as e:
            self.s_bot.message = "Exception at clean tables: " + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)


if __name__ == "__main__":
    s_time = ShTime.ClassTime()
    if s_time.string_to_time(time_string='00:00:00') <= s_time.string_to_time(
            time_string=str(s_time.now_time)) <= s_time.string_to_time(time_string='00:01:00'):
        ShynaTwelveAM().run_at_twelve()

#
# test = ShynaTwelveAM()
# test.clean_tables()
