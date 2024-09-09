# (확장용) 분석 결과 응답 dto
def simple_response_dto(url, phishing_result, phishing_prob):
    """Response Body에 맞는 DTO 생성."""

    return {
        "url": url,
        "prediction_result": int(phishing_result),  # 피싱 여부 (True/False)
        "prediction_prob": f"{phishing_prob}%",  # 피싱 확률
    }

# (웹용) 상세 분석 결과 응답 dto
def detailed_response_dto(url, phishing_result, phishing_prob, suspicious_features, ip_info):
    """Response Body에 맞는 DTO 생성."""

    return {
        "url": url,
        "prediction_result": int(phishing_result),  # 피싱 여부
        "prediction_prob": f"{phishing_prob}%",  # 피싱 확률
        "ip_address": ip_info["ip_address"],
        "country": ip_info["country"],
        "is_vpn": ip_info["is_vpn"],
        "isp_name": ip_info["isp_name"],
        "url_based_feature_list": suspicious_features["URL_based"],
        "content_based_feature_list": suspicious_features["Content_based"],
        "domain_based_feature_list": suspicious_features["Domain_based"]
    }