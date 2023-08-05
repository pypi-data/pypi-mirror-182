from gtja_vintex_qyt import GTJAVintexQyt

if __name__ == '__main__':
    vintex_qyt_client = GTJAVintexQyt("13158901580", "990818")
    print(vintex_qyt_client.qc0020("1").data)
    print(vintex_qyt_client.qc0020("3").data)
    print(vintex_qyt_client.qc0021().data)