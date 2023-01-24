# First-party imports
from accounts.models import UserProfile, Account


def run():
    """Create a UserProfile for all existing users.
    If already UserProfile exist then skip it"""

    # Fetch users who has UserProfile created
    user_ids_with_profile = UserProfile.objects.all().values_list(
        "user__id", flat=True
    )

    # Get Users without profile
    user_without_profile = Account.objects.exclude(id__in=user_ids_with_profile)

    # Bulk Create Profiles for these users
    profile_list = []
    for user in user_without_profile:
        profile = UserProfile(
            user=user,
            profile_picture="default/default-user.png",
        )
        profile_list.append(profile)

    UserProfile.objects.bulk_create(profile_list)


if __name__ == "__main__":
    run()
