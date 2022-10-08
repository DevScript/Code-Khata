// This file contains some prewritten code for custom widgets

// social icon buttons with custom shadow and elevation
class SocialIconButtonsRow extends StatelessWidget {
  const SocialIconButtonsRow({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        const SizedBox(),
        SocialButtonWithShadow(
          icon: FontAwesomeIcons.facebookF,
          color: const Color(0xFF4267B2),
          onPressed: () {},
        ),
        SocialButtonWithShadow(
          icon: FontAwesomeIcons.twitter,
          color: const Color(0xFF1DA1F2),
          onPressed: () {},
        ),
        SocialButtonWithShadow(
          icon: FontAwesomeIcons.googlePlusG,
          color: const Color(0xFFDB4437),
          onPressed: () {},
        ),
        const SizedBox(),
      ],
    );
  }
}

class SocialButtonWithShadow extends StatelessWidget {
  const SocialButtonWithShadow(
      {Key? key, required this.icon, required this.color, this.onPressed})
      : super(key: key);

  final Color color;
  final IconData icon;
  final Function()? onPressed;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 45,
      height: 45,
      child: TextButton(
        onPressed: onPressed,
        style: ButtonStyle(
          padding: MaterialStateProperty.all(const EdgeInsets.all(0)),
          elevation: MaterialStateProperty.resolveWith((states) {
            if (states.contains(MaterialState.pressed)) {
              return 0;
            } else {
              return 8;
            }
          }),
          shape: MaterialStateProperty.all(
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50))),
          backgroundColor: MaterialStateProperty.all(color),
          shadowColor: MaterialStateProperty.all(color),
        ),
        child: Icon(
          icon,
          color: Colors.white,
        ).p(8),
      ),
    );
  }
}

class SocialButtonWithShadow extends StatelessWidget {
  const SocialButtonWithShadow(
      {Key? key, required this.icon, required this.color, this.onPressed})
      : super(key: key);

  final Color color;
  final IconData icon;
  final Function()? onPressed;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 45,
      height: 45,
      child: TextButton(
        onPressed: onPressed,
        style: ButtonStyle(
          padding: MaterialStateProperty.all(const EdgeInsets.all(0)),
          elevation: MaterialStateProperty.resolveWith((states) {
            if (states.contains(MaterialState.pressed)) {
              return 0;
            } else {
              return 8;
            }
          }),
          shape: MaterialStateProperty.all(
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50))),
          backgroundColor: MaterialStateProperty.all(color),
          shadowColor: MaterialStateProperty.all(color),
        ),
        child: Icon(
          icon,
          color: Colors.white,
        ).p(8),
      ),
    );
  }
}

// stacked promo card design

class PromoContainer extends StatefulWidget {
  const PromoContainer({Key? key}) : super(key: key);

  @override
  State<PromoContainer> createState() => _PromoContainerState();
}

class _PromoContainerState extends State<PromoContainer>
    with SingleTickerProviderStateMixin {
  final List<double> xPaddings = [36, 28, 16];

  final List<double> opacityList = [0.8, 1, 1];
  final List<double> bottomMargin = [0, 10, 20];

  final List<Discount> _discounts = [
    Discount(),
    Discount(),
    Discount(),
  ];

  @override
  Widget build(BuildContext context) {
    return (_discounts.isEmpty)
        ? const SizedBox.shrink()
        : Stack(
            children: [
              for (int i = 0; i < _discounts.length; i++)
                Dismissible(
                  onDismissed: (v) {
                    setState(() {
                      _discounts.removeAt(i);
                      xPaddings.removeAt(0);
                      opacityList.removeAt(0);
                      bottomMargin.removeAt(0);
                    });
                  },
                  key: Key(i.toString()),
                  child: Align(
                      alignment: Alignment.topCenter,
                      child: AspectRatio(
                        aspectRatio: 16 / 8.5,
                        child: Opacity(
                          opacity: opacityList[i],
                          child: AnimatedContainer(
                            duration: const Duration(milliseconds: 200),
                            margin: EdgeInsets.only(
                              bottom: bottomMargin[i],
                            ),
                            decoration: BoxDecoration(
                                color: Theme.of(context).primaryColor,
                                image: const DecorationImage(
                                    image: AssetImage(Images.promoContainer)),
                                borderRadius: BorderRadius.circular(12)),
                            child: Stack(children: [
                              Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  const SizedBox(height: 20),
                                  'Flat ${i + 1}0% off'.text.semiBold.xl.make(),
                                  8.heightBox,
                                  'Avail Flat ${i}0% off on your first order We have awesome discount on your first order. Avail before it’s too late! 😃'
                                      .text
                                      .maxLines(3)
                                      .ellipsis
                                      .make()
                                      .pOnly(right: 24),
                                  const Spacer(),
                                  SecondaryButton(
                                      onPressed: () {}, text: 'Avail Discount'),
                                  const SizedBox(height: 16),
                                ],
                              ).px(16),
                            ]),
                          ).px(xPaddings[i]),
                        ),
                      )),
                ),
            ],
          ).p(12).py(16);
  }
}
